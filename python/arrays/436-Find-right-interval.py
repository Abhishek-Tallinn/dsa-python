# Problem: Leetcode 436 - Find right interval
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-right-interval/description/
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Approach: We sort the intervals for start and tthen a right interval can only be on the right of it.
# So then as soon as we find the right interval, we break the loop but before that we write the in the result array
# on the index that we get from original dictionary whose value we set to the index of the tuple found on index j

from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        #we can optimize by using binary search
        # where we keep index and make list of starts
        # then the end of original interval is bisected into the starts
        # to get the index
        d = {tuple(val):i for i,val in enumerate(intervals)}
        intervals.sort(key = lambda x:x[0])
        stack = []
        res = [-1]*len(intervals)
        for i in range(len(intervals)):
            for j in range(i,len(intervals)):
                if intervals[j][0] >= intervals[i][1]:
                    res[d[tuple(intervals[i])]] = d[tuple(intervals[j])]
                    break


        return res
        


        '''
        naive - O(n^2) - TLE
        res = [-1]*len(intervals)
        
        for i in range(len(intervals)):
            mn_start = float('inf')
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[j][0] >= intervals[i][1]:
                    if intervals[j][0] < mn_start:
                        mn_start = intervals[j][0]
                        res[i] = j
        return res
        '''