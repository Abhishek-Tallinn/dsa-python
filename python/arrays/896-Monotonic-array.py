# Problem: Leetcode 896 - Monotonic array
# Difficulty: Easy
# Link: https://leetcode.com/problems/monotonic-array/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n)
# Approach: we sort in both direction and check if any of the conditions is true then its True else its false

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums==sorted(nums,reverse=True)