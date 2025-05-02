--177. Nth Highest Salary
--Solved
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
--Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.
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
--n = 2
--Output: 
--+------------------------+
--| getNthHighestSalary(2) |
--+------------------------+
--| 200                    |
--+------------------------+
--Example 2:
--
--Input: 
--Employee table:
--+----+--------+
--| id | salary |
--+----+--------+
--| 1  | 100    |
--+----+--------+
--n = 2
--Output: 
--+------------------------+
--| getNthHighestSalary(2) |
--+------------------------+
--| null                   |
--+------------------------+


CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
       SELECT (select TOP 1 e1.salary as 'getNthHighestSalary(2)' from (SELECT ID,SALARY, DENSE_RANK() OVER(ORDER BY SALARY DESC) as 'salaryrank' from Employee) as e1 where e1.salaryrank=@N) as 'getNthHighestSalary(2)'

    );
END


-- CTE
CREATE FUNCTION getNthHighestSalary(@N INT)
RETURNS INT
AS
BEGIN
    DECLARE @Result INT;

    WITH RANKED_SALARY AS (
        SELECT SALARY, DENSE_RANK() OVER (ORDER BY SALARY DESC) AS salaryrank
        FROM Employee
    )
    SELECT @Result = SALARY
    FROM RANKED_SALARY
    WHERE salaryrank = @N;

    RETURN @Result;
END

-- USING OFFSET
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        OFFSET @N-1 ROWS FETCH NEXT 1 ROWS ONLY            
    );
END
