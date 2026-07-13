-- Problem: Leetcode 1468 - Calculate salaries
-- Difficulty: Medium
-- Link: https://leetcode.com/calculate-salaries/description/
-- Approach: We can use a cross join to join a max salary to every row in salaries table but the issue is
-- that we have to find max salary as per companies. SO we use a CTE and find the max salary for each compnay.
-- then we use usual query and join this max salary table to salaries and then do the cases to apply relevant tax

with max_salary as (
    select company_id,MAX(salary) as mx
    from Salaries
    group by company_id
)
select s1.company_id,s1.employee_id,s1.employee_name, 
        (CASE
        WHEN mx < 1000 THEN SALARY
        WHEN mx >=1000 AND  mx<= 10000 THEN ROUND(SALARY * 0.76,0)
        WHEN mx > 10000 THEN ROUND(SALARY * 0.51,0)
        END) as salary
FROM Salaries s1
join max_salary m
on s1.company_id = m.company_id;