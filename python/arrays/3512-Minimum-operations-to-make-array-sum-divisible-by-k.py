# Problem: Leetcode 3512 - Minimum operations to make array sum divisible by k
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/
# Time Complexity: O(n) as we have to calculate the sum 
# Space Complexity: O(1)
# Approach: We need to calculate the max multiple of k which is just let than sum of nums and return the difference between the two

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        return s - (k * (s//k))