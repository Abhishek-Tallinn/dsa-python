-- Problem: Leetcode 177 - Nth Highest Salary
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/nth-highest-salary/description/
-- Approach: we use a subquery to find the nth highest distinct salary in the Employee table
-- as we want to return null if nth highest salary does not exist and we use a function to get the nth highest salary.



CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N-1;

  RETURN (
      SELECT DISTINCT salary AS getNthHighestSalary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END