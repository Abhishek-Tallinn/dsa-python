-- Problem: Leetcode 1148 - Article views I
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/article-views-i/description/
-- Approach: We simply select the distinct author id's where author and viewer id is same
-- and then we just sort then

select DISTINCT author_id as id
from Views 
where author_id = viewer_id
order by id ASC;