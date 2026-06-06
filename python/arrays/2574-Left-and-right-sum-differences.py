# Problem: Leetcode 2574 - Left and Right Sum Differences
# Difficulty: Easy
# Link: https://leetcode.com/problems/left-and-right-sum-differences/description/
# Time Complexity: O(n) where n is the length of the input array
# Space Complexity: O(n) which is unavoidable as we have to build answer array.
# Approach: Calculate the total sum of the array, then iterate through each element, maintaining a running left sum and calculating the right sum as the difference between the total and the left sum.

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        ans = [0]*len(nums)
        for i in range(len(nums)):
            total -= nums[i]
            ans[i] = abs(total-left_sum)
            left_sum += nums[i]
        return ans
