-- Problem: Leetcode 1873 - Calculate special bonus
-- Difficulty: Easy
-- Link: https://leetcode.com/calculate-special-bonus/description/
-- Approach: We simply take employee id and apply case based filter to filter the salary as bonus and return the result
-- there is also a second join based solution that make a special table with bonus only and then joins it back to main table
-- where we can just select the bonus from column directly but it is slower.

select employee_id, case when employee_id%2=1 and SUBSTRING(name,1,1)!='M' then salary else 0 end as bonus
from Employees
order by employee_id;

/* subquery based solution which is slow
select e.employee_id,  temp.b as bonus
from Employees e
join (
    select e1.employee_id , (case when employee_id%2=1 and SUBSTRING(name,1,1)!='M' then e1.salary else 0 end) as b
    from Employees e1
) temp
on e.employee_id = temp.employee_id
order by temp.employee_id;
*/