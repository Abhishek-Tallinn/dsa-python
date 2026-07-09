-- Problem: Leetcode 1378 - Replace employee ID with unique identifier
-- Difficulty: Easy
-- Link: https://leetcode.com/replace-employee-id-with-unique-identifier/description/
-- Approach: We simply join the tables on id match and any employees which dont have a match
-- automatically have their unique ID value as null

select e1.unique_id, e.name as name
from Employees e
left join EmployeeUNI e1
on e.id = e1.id;