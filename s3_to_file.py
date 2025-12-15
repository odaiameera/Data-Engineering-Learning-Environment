#!/usr/bin/env python3
"""
Download objects from an S3 bucket to a local directory or a single zip file.

Usage examples:
  - Save bucket contents to a directory:
      python s3_to_file.py --bucket my-bucket --dest ./downloaded

  - Save bucket contents into a zip file:
      python s3_to_file.py --bucket my-bucket --zip bucket_contents.zip

This script uses boto3 and respects AWS credentials configured in the environment
or via named profiles (use `--profile PROFILE_NAME`).
"""
from __future__ import annotations

import argparse
import os
import sys
import zipfile
from typing import Iterable, Dict

import boto3
import botocore


def list_objects(s3_client, bucket: str, prefix: str | None) -> Iterable[Dict]:
    paginator = s3_client.get_paginator("list_objects_v2")
    pagination_params = {"Bucket": bucket}
    if prefix:
        pagination_params["Prefix"] = prefix

    for page in paginator.paginate(**pagination_params):
        for obj in page.get("Contents", []):
            yield obj


def download_object_to_dir(s3_client, bucket: str, key: str, dest_root: str) -> None:
    if key.endswith("/"):
        return
    dest_path = os.path.join(dest_root, *key.split("/"))
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    try:
        s3_client.download_file(bucket, key, dest_path)
    except botocore.exceptions.BotoCoreError as e:
        print(f"ERROR downloading {key}: {e}", file=sys.stderr)


def stream_objects_to_zip(s3_client, bucket: str, objects: Iterable[Dict], zip_path: str) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for obj in objects:
            key = obj["Key"]
            if key.endswith("/"):
                continue
            print(f"Adding to zip: {key}")
            try:
                resp = s3_client.get_object(Bucket=bucket, Key=key)
                body = resp["Body"]
                # Write streamed content into the zip member to avoid storing whole object in memory
                with zf.open(key, "w") as member:
                    for chunk in iter(lambda: body.read(1024 * 1024), b""):
                        member.write(chunk)
            except botocore.exceptions.BotoCoreError as e:
                print(f"ERROR adding {key} to zip: {e}", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download S3 bucket contents to a directory or a zip file")
    p.add_argument("--bucket", required=True, help="S3 bucket name")
    p.add_argument("--prefix", default=None, help="Optional prefix to filter objects")
    p.add_argument("--dest", default="./s3_download", help="Destination directory for downloaded files")
    p.add_argument("--zip", dest="zip", default=None, help="Write all objects into this zip file instead of a directory")
    p.add_argument("--profile", default=None, help="AWS profile name to use (optional)")
    p.add_argument("--region", default=None, help="AWS region (optional)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    session_kwargs = {}
    if args.profile:
        session_kwargs["profile_name"] = args.profile
    if args.region:
        session_kwargs["region_name"] = args.region

    try:
        session = boto3.Session(**session_kwargs) if session_kwargs else boto3.Session()
        s3 = session.client("s3")
    except botocore.exceptions.BotoCoreError as e:
        print(f"ERROR creating boto3 session: {e}", file=sys.stderr)
        return 2

    objects_iter = list_objects(s3, args.bucket, args.prefix)

    # If writing to zip, we must re-iterate objects; convert to list to allow two passes.
    objects = list(objects_iter)
    if not objects:
        print("No objects found with the given bucket/prefix.")
        return 0

    if args.zip:
        print(f"Writing {len(objects)} objects from bucket '{args.bucket}' to zip '{args.zip}'")
        stream_objects_to_zip(s3, args.bucket, objects, args.zip)
        print("Zip file created.")
    else:
        print(f"Downloading {len(objects)} objects from bucket '{args.bucket}' to directory '{args.dest}'")
        for obj in objects:
            key = obj["Key"]
            print(f"Downloading: {key}")
            download_object_to_dir(s3, args.bucket, key, args.dest)
        print("Download complete.")
