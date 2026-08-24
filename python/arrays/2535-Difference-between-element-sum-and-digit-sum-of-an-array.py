# Problem: Leetcode 2535 - Difference between element sum and digit sum of an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-distance-to-target-string-circular-array/description/
# Time Complexity: O(n) as we do two loops to find the respective sums
# Space Complexity: O(1) as we only use two pointers
# Approach: We calculate the respective sums and return the absolute difference

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        ds = sum([int(d) for num in nums for d in str(num)])

        return abs(s-ds)