-- Problem: Leetcode 577 - Employee Bonus
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/employee-bonus/description/
-- Approach: we use a LEFT JOIN to find employees who have no corresponding bonus in the Bonus table by filter on NULL
-- as well as employees who have bonus less than 1000 using the 'or' condition.



select e.name,b.bonus
from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus IS NULL;