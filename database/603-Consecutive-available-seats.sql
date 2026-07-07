-- Problem: Leetcode 603 - Consecutive Available Seats
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/consecutive-available-seats/description/
-- Approach: Since we need to check different rows of same table a self join is necessary but also since we have to check the row before 
-- as well as the row after for each we join on both id+1 and id-1 and we use or as using AND will lead to no result as both conditions cannot be true at the same time
select DISTINCT c.seat_id
from Cinema c
join Cinema d
ON c.seat_id = d.seat_id+1 or c.seat_id = d.seat_id-1
where c.free = 1 and c.free = d.free
order by seat_id;