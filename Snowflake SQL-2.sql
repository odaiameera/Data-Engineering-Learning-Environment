-- This file was made to test Snowflake SQL queries on VS Code with the Snowflake extension.
USE DATABASE GOOGLE_DB;
SELECT *    
FROM EMPLOYEES
WHERE AGE >= 30 AND AGE <= 40;

USE DATABASE VSCODE_1;
Create table Table_1 ( Name VARCHAR,
age INT,
city VARCHAR,
sex VARCHAR,
job VARCHAR,
salary FLOAT);

ALTER TABLE CSI_AGENTS RENAME TO EMPLOYEES;