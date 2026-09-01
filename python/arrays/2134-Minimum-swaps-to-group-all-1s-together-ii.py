# Problem: Leetcode 2134 - Minimum Swaps to Group All 1's Together II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a sliding window of size equal to the number of 1's in the array as the window.
# For each window, count the number of 0's - which is done in O(1) due to prefix sum.(which represents swaps needed). 
# Return the minimum swaps across all windows. To check all rotated windows we double the array which can be handled 
# as the size will be 2x10^5 which is allowed. Then we run the main loop till n as we only need n starting positions.

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window = sum(nums)
        nums = nums+nums
        swaps = float('inf')
        prefix = [0]*(len(nums)+1)
        zeros = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            prefix[i+1] = zeros
        for i in range(0,n):
            swaps = min(swaps,prefix[i+window] - prefix[i])
        return swaps 