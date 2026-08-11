# Problem: Leetcode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/
# Time Complexity: O(n logn) - as we go through all the element of from 1 to max and we are also sorting the list
# Space Complexity: O(n) as we make a new sorted list
# Approach1: we simply find the index till there is a sequential prefix and sum it. Then we make a set of nums for quick loop up
# and iterate the sum values from the actual sum to max value of 50*50 and return the first value that is not in the set. This will be the smallest missing integer greater than sequential prefix sum.

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        i = 0
        while i<len(nums)-1:
            if nums[i] + 1 == nums[i+1]:
                i+=1
            else:
                break
        total = sum(nums[:(i+1)])
        for num in range(total,50*50):
            if num not in s:
                return num
