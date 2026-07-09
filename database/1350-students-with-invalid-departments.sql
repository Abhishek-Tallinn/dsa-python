-- Problem: Leetcode 1350 - Students with invalid departments
-- Difficulty: Easy
-- Link: https://leetcode.com/students-with-invalid-departments/description/
-- Approach: We can do it with two ways where we check direclty if the department id of student
-- does not exist in the Departments table and also by 
-- joining both and then checking if department.name for any student is NULL as there is no match.

select s.id,s.name
from Students s
where s.department_id NOT IN (
    select id
    FROM Departments
);

/*
select s.id,s.name 
from Students s
left join Departments d
on s.department_id = d.id
where d.name IS NULL;
*/