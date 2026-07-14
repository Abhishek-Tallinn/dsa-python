-- Problem: Leetcode 2377 - Sort the olympic table
-- Difficulty: Easy
-- Link: https://leetcode.com/sort-the-olympic-table/description/
-- Approach: Simple question that teaches grouping the sorting criteria

select * 
from Olympic 
order by gold_medals DESC,silver_medals DESC,bronze_medals DESC,country;