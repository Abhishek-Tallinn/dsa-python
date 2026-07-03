-- Problem: Leetcode 176 - Second Highest Salary
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/second-highest-salary/description/
-- Approach: we use a subquery to find the second highest distinct salary in the Employee table
-- as we want to return null if second highest salary does not exist


SELECT(
    SELECT DISTINCT salary 
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;