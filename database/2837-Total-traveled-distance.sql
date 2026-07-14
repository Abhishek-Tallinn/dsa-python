-- Problem: Leetcode 2837 - Total traveled distance
-- Difficulty: Easy
-- Link: https://leetcode.com/total-traveled-distance/description/
-- Approach: We need to just join the table on user_id and then group by user_id and take sum of total distance
-- and use coalesce to return 0 where the value is null

select u1.user_id,u1.name,COALESCE(SUM(r.distance),0) as `traveled distance`
from Users u1
left join Rides r
    ON u1.user_id = r.user_id
group by user_id
order by user_id;