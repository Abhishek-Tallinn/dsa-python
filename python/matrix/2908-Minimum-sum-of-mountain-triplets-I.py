# Problem: Leetcode 2908 - Minimum sum of mountain triplets I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-sum-of-mountain-triplets-I/description/
# Time Complexity: O(n^3)
# Space Complexity: O(1)
# Approach: We do a nested for loop to find the mountain triplets

from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mn = float('inf')
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[j] > nums[i]:
                    for k in range(j+1,len(nums)):
                        if nums[j] > nums[k]:
                            mn = min(mn, nums[i]+nums[j] + nums[k])
        return -1 if mn==float('inf') else mn