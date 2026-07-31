# Problem: Leetcode 561 - Array partition
# Difficulty: Easy
# Link: https://leetcode.com/problems/array-partition/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: to maximize the min of pairs we sort and make sure we the best values possible
# by iterating by jumps of two

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        total = 0
        for i in range(0,len(nums),2):
            total+=nums[i]
        return total