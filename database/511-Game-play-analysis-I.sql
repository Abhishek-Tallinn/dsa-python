-- Problem: Leetcode 511 - Game play Analysis I
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/game-play-analysis-i/description/
-- Approach: we select the player_id and the minimum event_date as first_login from the Activity table, grouping by player_id and ordering by player_id in ascending order.

SELECT player_id,MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
ORDER BY player_id ASC;