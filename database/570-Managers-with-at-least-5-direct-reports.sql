-- Problem: Leetcode 570 - Managers with at least 5 direct reports
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/
-- Approach: we's select the name after permorning a self join on id and manager ID and just counting which
-- row appears at least 5 time

select e.name as name
from Employee e
join Employee f
    on e.id = f.managerId
    group by e.id
    having COUNT(*) >= 5;