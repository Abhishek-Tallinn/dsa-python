-- Problem: Leetcode 534 - Game play Analysis III
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/game-play-analysis-iii/description/
-- Approach: we select the played_id, event_date and using a running subquery we get the sum of games_played for that player_id where the event_date 
--is less than or equal to the current row's event_date. This gives us the running total of games played so far for each player.


SELECT a.player_id,a.event_date,
    (SELECT SUM(games_played) 
    From Activity b
    where b.player_id = a.player_id
    and b.event_date <= a.event_date) as games_played_so_far
from Activity a;