# Apply Filters to SQL Queries
## Project Description
As a security professional, I am responsible for ensuring the integrity of organizational data and investigating potential security incidents. In this project I used SQL to filter through large datasets in the `employees` and `log_in_attempts` tables. My objective was to identify suspicious login activity and extract specific employee lists for critical security updates based on department and office location.

## Retrieve After-Hours Failed Login Attempts
I discovered a potential security incident that occurred after business hours (18:00). To investigate, I needed to find all failed login attempts that happened after this time.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = 0;
```
**How it works:** The `SELECT *` statement pulls all columns from the `log_in_attempts` table. The `WHERE` clause uses the `AND` operator to combine two conditions: `login_time > '18:00'` filters for evening activity, and `success = 0` (or `FALSE`) filters for attempts that were not successful.

## Retrieve Login Attempts on Specific Dates
A suspicious event was reported on 2022-05-09. I needed to review all login attempts from that day and the day prior (2022-05-08) to check for a pattern of behavior.
```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-08' OR login_date = '2022-05-09';
```
**How it works:** This query retrieves all records where the `login_date` matches either of the two specified dates. Using the `OR` operator allows the query to return results for both days simultaneously.

## Retrieve Login Attempts Outside of Mexico
The security team confirmed that recent suspicious activity did not originate from Mexico. To narrow my search, I filtered for login attempts from all other countries.
```sql
SELECT *
FROM log_in_attempts
WHERE country NOT LIKE 'MEX%';
```
**How it works:** The `NOT LIKE` operator is used to exclude specific patterns. Since the data refers to Mexico as both "MEX" and "MEXICO," I used the`%` wildcard after "MEX" to ensure any variation starting with those three letters was filtered out.

## Retrieve Employees in Marketing and East Building
The organization required a security update specifically for machines used by the Marketing department in the East building.
```sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
```
**How it works:** This query uses `AND` to ensure both conditions are met. The `office LIKE 'East%'` filter captures all offices located in the East building (e.g., East-170, East-320) by using the`%` wildcard to match any characters following the word "East."

## Retrieve Employees in Sales or Finance
A different security update was needed for all employees in either the Sales or Finance departments.
```sql
SELECT *
FROM employees
WHERE department = 'Sales' OR department = 'Finance';
```
**How it works:** The `OR` operator is applied here to include any employee who belongs to either the Sales department or the Finance department. This ensures that the results contain the combined list of both teams.

## Retrieve All Employees Not in IT
Finally, I needed to identify all employees who are **not** in the Information Technology department, as the IT department had already received their security updates.
```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```
**How it works:** The `NOT` operator is used to exclude a specific criteria. By applying it to the `department = 'Information Technology'` condition, the query returns every employee in the organization except those in IT.

## Summary
In this activity, I utilized SQL filters to investigate security logs and organize employee data for system maintenance. By using operators like `AND`, `OR`, `NOT`, and `LIKE`, I was able to transition from broad datasets to specific, actionable information. These queries allowed me to isolate suspicious login attempts by time and location, as well as efficiently target specific employee groups for required security patches.