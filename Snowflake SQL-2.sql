-- This file was made to test Snowflake SQL queries on VS Code with the Snowflake extension.
USE DATABASE GOOGLE_DB;
SELECT *    
FROM EMPLOYEES
WHERE AGE >= 30 AND AGE <= 40;