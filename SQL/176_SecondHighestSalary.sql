--176. Second Highest Salary
--Medium
--Topics
--Companies
--SQL Schema
--Pandas Schema
--Table: Employee
--
--+-------------+------+
--| Column Name | Type |
--+-------------+------+
--| id          | int  |
--| salary      | int  |
--+-------------+------+
--id is the primary key (column with unique values) for this table.
--Each row of this table contains information about the salary of an employee.
-- 
--
--Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
--
--The result format is in the following example.
--
-- 
--
--Example 1:
--
--Input: 
--Employee table:
--+----+--------+
--| id | salary |
--+----+--------+
--| 1  | 100    |
--| 2  | 200    |
--| 3  | 300    |
--+----+--------+
--Output: 
--+---------------------+
--| SecondHighestSalary |
--+---------------------+
--| 200                 |
--+---------------------+
--Example 2:
--
--Input: 
--Employee table:
--+----+--------+
--| id | salary |
--+----+--------+
--| 1  | 100    |
--+----+--------+
--Output: 
--+---------------------+
--| SecondHighestSalary |
--+---------------------+
--| null                |
--+---------------------+

-- Using window function
SELECT (select TOP 1 e1.salary as 'SecondHighestSalary' from (SELECT ID,SALARY, DENSE_RANK() OVER(ORDER BY SALARY DESC) as 'salaryrank' from Employee) as e1 where e1.salaryrank=2) as 'SecondHighestSalary'

-- Using offset and fetch next
select (SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY
) as 'SecondHighestSalary'
