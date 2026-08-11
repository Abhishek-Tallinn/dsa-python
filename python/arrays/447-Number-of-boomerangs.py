# Problem: Leetcode 447 - Number of boomerangs
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-boomerangs/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We use take each point and record its distance with every other points. Then for each distance
# the number of points with which equidistant can be acheived is k*k-1. example if there is only one distance of 5 meaning
# that only one point is at a distance of 5 and no one else so our boomerang condition will not hold.
# in this case k*(k-1) will give us 1*0 which is 0.

import math
from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return (x2-x1)**2 + (y2-y1)**2
        cnt = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    di = dist(points[i],points[j])
                    d[di]+=1

            for v in d.values():
                cnt += v*(v-1)
        return cnt