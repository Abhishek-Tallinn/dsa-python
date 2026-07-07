-- Problem: Leetcode 610 - Triangle Judgement
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/triangle-judgement/description/
-- Approach: We simply check the triangle inequality theorem which states that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side. If this condition is satisfied for all three combinations of sides, then the three lengths can form a triangle.
-- and we make the check for each row in the Triangle table and return 'Yes' if they can form a triangle and 'No' otherwise.

select x,y,z,
    CASE 
        WHEN x+y > z
            AND y+z > x
            AND x+z > y
            THEN 'Yes'
            ELSE 'No'
        END as triangle
from Triangle;