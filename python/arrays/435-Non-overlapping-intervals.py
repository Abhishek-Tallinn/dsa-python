# Problem: Leetcode 435 - Non overlapping intervals
# Difficulty: Medium
# Link: https://leetcode.com/problems/non-overlapping-intervals/description/
# Time Complexity: O(n log n)
# Space Complexity: O(n)  
# Approach: We sort the intervals and check for overlap. whenever overlap is found we increment count as we have to drop one of the overlapping intervals
# but we have to drop the one which will cause the least overlaps as the idea is to keep cnt to a minimum.
# we do this by updating our mx to the min value of the ending right value of the two overlapping intervals so that we reduce overlap chances
# in other case if overlap is not found we just update our mx variable to check for overlaps in the intervals ahead

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        mx = intervals[0][1]
        cnt = 0
        for right in range(1,len(intervals)):
            if mx > intervals[right][0]:
                mx = min(mx,intervals[right][1])
                cnt+=1
            else:
                mx = intervals[right][1]
        return cnt