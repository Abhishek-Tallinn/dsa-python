# Problem: Leetcode 396 - Rotate Function
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-function/description/
# Time Complexity: O(n)
# Space Complexity: O(n) with O(n) extra space for the doubled array. 
# Approach: Since we have to rotate the array we simulate it by doubling the array and running a sliding window on it with 2 pointers.

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        dnums = nums+nums
        value = 0
        left = 0
        sum_of_window = sum(nums)
        for i in range(n):
            value+=i*nums[i]
        max_value = value
        for right in range(n,len(dnums)):
            value = value + dnums[right]*(n-1) - (sum_of_window-dnums[left])
            left+=1
            max_value = max(max_value,value)
        return max_value