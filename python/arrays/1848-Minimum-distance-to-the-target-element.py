# Problem: Leetcode 1848 - Minimum Distance to the Target Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-distance-to-the-target-element/description/
# Time Complexity: O(n) as we iterate through the array once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We iterate through the array and keep track of the mn absolute value of i-start
# and return the minimum value at the end.

from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mn = float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                mn = min(mn,abs(i-start))
        return mn