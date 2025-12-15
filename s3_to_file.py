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