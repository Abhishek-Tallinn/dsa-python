-- Problem: Leetcode 1075 - Project employees - I
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/product-employees-i/description/
-- Approach: We simple join the tables on employee id and then group by the project_id 
-- so that we can calculate avg experience years for total employees

select p.project_id,ROUND(AVG(e.experience_years),2) as average_years
from Project p
join Employee e
on p.employee_id = e.employee_id
group by project_id;