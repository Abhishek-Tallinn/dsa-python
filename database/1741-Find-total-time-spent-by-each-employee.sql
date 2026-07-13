-- Problem: Leetcode 1741 - Find total time spent by each employee
-- Difficulty: Easy
-- Link: https://leetcode.com/find-total-time-spent-by-each-employee/description/
-- Approach: We simply group by event_day and emp_id which forms a unique row and then 
-- perform sum on out_time and in_time for those rows and return the result

select event_day as day, emp_id,sum(out_time-in_time) as total_time
from Employees
group by emp_id,event_day;