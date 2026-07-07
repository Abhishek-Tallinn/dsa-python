-- Problem: Leetcode 1050 - Actors and Directors Who Cooperated At Least 3 Times
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-3-times/description/
-- Approach: We select the actor_id and director_id from the ActorDirector table, group by these columns, and filter for pairs that have cooperated at least 3 times.

select actor_id,director_id 
from ActorDirector
group by actor_id,director_id
having count(*)>2;