-- Problem: Leetcode 620 - Not Boring Movies
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/not-boring-movies/description/
-- Approach: we select the id, movie, description, and rating from the Cinema table and filter for movies with an odd id and a description that is not 'boring'.
-- It is a simple straighforward query.


SELECT m.id,m.movie,m.description,m.rating
FROM Cinema m
WHERE m.id % 2 = 1 and m.description != "boring"
ORDER BY m.rating DESC;