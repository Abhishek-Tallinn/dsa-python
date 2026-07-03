-- Problem: Leetcode 181 - Employees Earning More Than Their Managers
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
-- Approach: we use a self JOIN to compare each employee's salary with their manager's salary
-- to find employees who earn more than their managers.


SELECT e.name as Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;