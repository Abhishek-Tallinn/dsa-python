-- Problem: Leetcode 2687 - Bikes last time used
-- Difficulty: Easy
-- Link: https://leetcode.com/bikes-last-time-used/description/
-- Approach: Just group by bike and select the max end time from each group and the return in desc order

select bike_number,MAX(end_time) as end_time
from Bikes
group by bike_number
order by end_time DESC;