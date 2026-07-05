-- Problem: Leetcode 512 - Game play Analysis II
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/game-play-analysis-ii/description/
-- Approach: we select the player_id and device_id from the Activity table and filter for rows where the event_date is equal to the minimum event_date for that player_id.

--subquery is running for each row. 
--so one row is taken and its date is checked with date returned 
--from the subquery. If it matches we keep it else we discard

SELECT a.player_id, a.device_id
FROM Activity a
WHERE a.event_date = 
    (
        SELECT MIN(event_date)
        from Activity b
        where a.player_id = b.player_id
    );

