-- Problem: Leetcode 184 - Department Highest Salary
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/department-highest-salary/description/
-- Approach: we join the Employee and Department tables, then use a subquery to find the maximum salary in each department.
-- Finally, we filter the results to only include employees with the maximum salary in their respective departments.


SELECT d.name as Department, 
        e.name as Employee,
        e.salary as Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
JOIN(
    SELECT departmentId, MAX(salary) as MaxSalary
    FROM Employee 
    GROUP BY departmentId
) m 
ON e.departmentId= m.departmentId
AND e.salary = m.MaxSalary;