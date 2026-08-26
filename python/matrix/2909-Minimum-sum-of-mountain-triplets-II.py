# Problem: Leetcode 2909 - Minimum sum of mountain triplets II
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-sum-of-mountain-triplets-II/description/
# Time Complexity: O(n) as we precompute the min value via suffix sum seen beyond the current index i
# Space Complexity: O(n) since we compute suffix
# Approach: Since the total min value needed has to be lowest we need the min left and right values. for each index we keep a check on min seen on its left till now
# and the minimum value to the right of current index is known by the prefix sum. Then we keep updating the mn_sum in total

from typing import List
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mn_sum = float('inf')
        n = len(nums)
        min_right = [float('inf')] * (n + 1)
        min_left = float('inf')
        right = ['inf'] * (n + 1)
        for i in range(n - 1, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        for i,num in enumerate(nums):
            if min_left < num and min_right[i+1] < num:
                s = min_left + num + min_right[i+1]
                mn_sum = min(mn_sum,s)
            min_left = min(min_left,num)
        return -1 if mn_sum == float('inf') else mn_sum