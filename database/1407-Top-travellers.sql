-- Problem: Leetcode 1407 - Top travellers
-- Difficulty: Easy
-- Link: https://leetcode.com/top-travellers/description/
-- Approach: We first create a derived table with the total distance of each person then left join user 
-- table with it on id=user_id and the we use multiple orderBY statements in succession for tie break.

select u.name , COALESCE(total_distance.d,0) as travelled_distance
from Users u
left join 
    ( 
    select user_id,sum(distance) as d
    from Rides
    group by user_id
    ) total_distance

on u.id = total_distance.user_id
order by travelled_distance DESC,u.name ASC;