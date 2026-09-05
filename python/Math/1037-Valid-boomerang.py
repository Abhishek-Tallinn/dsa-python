# Problem: Leetcode 1037 - Valid Boomerang
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-boomerang/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We just need to check if the three points are colinear or not. We can do it manually by checking the slope between point 1 and point 2
# and the slope between point2 and point 3. If they are equal then they are colinear. but there is problem of division by zero error.
# so we check those cases separately.
# Approach2: A more efficient way is to take 2D cross product of the two vectors p0->p1 and p0->p2. Their cross product is the area of the signed paralellogram they form
# If points are colinear this paralellogram area will be 0.

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x0, y0), (x1, y1), (x2, y2) = points
        cross = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
        return cross != 0
        '''
        Original
        if points[0]==points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        if (points[1][0] == points[0][0]): 
            if points[2][0] == points[1][0]:
                return False
            return True
        if (points[2][0] == points[1][0]):
            if points[1][0] == points[0][0]:
                return False
            return True
        if ((points[1][1] - points[0][1]) / (points[1][0] - points[0][0])) == ((points[2][1]-points[1][1]) / (points[2][0] - points[1][0])):
            return False
        return True 
        '''