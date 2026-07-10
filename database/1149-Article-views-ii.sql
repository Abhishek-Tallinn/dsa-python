-- Problem: Leetcode 1148 - Article views II
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/article-views-ii/description/
-- Approach: We simply group by the pair of viewer_id and view_date and then we see if distinct article count is > 1 
-- and we return DISTINCT viewer ID then


select DISTINCT viewer_id as id
from Views
group by viewer_id,view_date
having COUNT(DISTINCT article_id) > 1;