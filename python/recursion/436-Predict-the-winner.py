# Problem: Leetcode 436 - Predict the Winner
# Difficulty: Medium
# Link: https://leetcode.com/problems/predict-the-winner/description/
# Time Complexity: O(n^2) where n is the length of the array
# Space Complexity: O(n^2) for the memoization table
# Approach: Use dynamic programming with memoization to calculate the maximum difference a player can achieve over their opponent in any subarray.
# Then we can return the list. we use a recursion tree to represent a choice at each stage.

from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(left,right):
            if left>right:
                return 0
            choose_left = nums[left] - dfs(left+1,right)
            choose_right = nums[right] - dfs(left,right-1)
            return max(choose_left,choose_right)
        return dfs(0,len(nums)-1) >= 0