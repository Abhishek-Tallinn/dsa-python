# Problem: Leetcode 495 - Teemo attacking
# Difficulty: Easy
# Link: https://leetcode.com/problems/teemo-attacking/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: For each time in timeseries we check the time of next attack. if the difference between the two
# is larger than duration then we take duration for the current attack poisoning otherwise we take the difference between the two time series i and i+1

from typing import List 

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries)-1):
            total+=min(duration,timeSeries[i+1]-timeSeries[i])
        total+=duration
        return total