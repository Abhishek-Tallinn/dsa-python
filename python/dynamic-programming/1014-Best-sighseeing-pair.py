# Problem: Leetcode 1014 - Best sightseeing pair
# Difficulty: Medium
# Link: https://leetcode.com/problems/best-sightseeing-pair/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only keep last state
# Approach: We use dynamic programming to keep track of max left+values[left] seen so far and calculate score 
# by adding that to current value - its index. then we update our max score.

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mx_score = 0 
        max_left_score = 0
        for j,val in enumerate(values):
            score = max_left_score + val - j
            mx_score = max(mx_score,score)
            max_left_score = max(max_left_score, j + val)
        return mx_score
        


        #brute forcing 
        # TLE
        '''
        mx = 0
        for i in range(len(values)-1):
            for j in range(i+1,len(values)):
                mx = max(mx, values[j]+values[i] + i - j)
        return mx
        '''