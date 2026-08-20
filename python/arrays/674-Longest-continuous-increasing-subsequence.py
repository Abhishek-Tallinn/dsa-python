# Problem: Leetcode 674 - Longest continous increasing subsequence
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
# Time Complexity: O(n) as run two pointers
# Space Complexity: O(1)
# Approach: We iterate on array and keep taking length of max subarray. if nums[right] <= nums[right-1] we update the left pointer

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        mx = 1
        for right in range(1,len(nums)):  
            if nums[right] <= nums[right-1]:
                left=right
            else:
                mx = max(mx,right-left+1)
        return mx
        