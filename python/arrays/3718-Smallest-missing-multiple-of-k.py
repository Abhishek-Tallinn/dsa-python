# Problem: Leetcode 3718 - Smallest missing multiple of k
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: make a set for look up and run a loop with multiples of k and check if they are not in nums
from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        constant = k
        while k in nums:
            k+=constant
        return k
