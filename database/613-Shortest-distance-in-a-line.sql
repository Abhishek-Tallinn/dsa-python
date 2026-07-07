-- Problem: Leetcode 613 - Shortest Distance in a Line
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/shortest-distance-in-a-line/description/
-- Approach: We need to find the shortest distance between any two points on a line. 
-- This can be done by calculating the absolute difference between the x-coordinates of all pairs of points and selecting the minimum.
-- We join tables on each non equal value to its O(n^2) time complexity


select MIN(ABS(p1.x - p2.x))  as shortest
from Point p1
join Point p2
on p1.x!=p2.x;