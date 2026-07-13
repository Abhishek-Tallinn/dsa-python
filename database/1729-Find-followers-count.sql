-- Problem: Leetcode 1729 - Find followers count
-- Difficulty: Easy
-- Link: https://leetcode.com/find-followers-count/description/
-- Approach: Very simple question where we just group and count the total in each group

select user_id,count(*) as followers_count
from Followers
group by user_id
order by user_id ASC;