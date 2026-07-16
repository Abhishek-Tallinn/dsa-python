-- Problem: Leetcode 612 - Shortest distance in a plane
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/shortest-distance-in-a-plane/description/
-- Approach: we join the tables on both x and y not being equal so we basically join each point with one another 
-- except with the exact same point and then we can calculate the shortest distance


select ROUND(MIN(SQRT(abs(x-x2)*abs(x-x2) + abs(y-y2)*abs(y-y2))),2) as shortest
from (
    select p1.x,p1.y,p2.x as x2,p2.y as y2
    from Point2D p1
    inner join Point2D p2 
    on p1.x <> p2.x or p1.y <> p2.y 
    ) t;
    