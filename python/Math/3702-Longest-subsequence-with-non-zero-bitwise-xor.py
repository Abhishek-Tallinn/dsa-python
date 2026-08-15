# Problem: Leetcode 3702 - Longest subsequence with non zero bitwise xor
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we dont have a set
# Approach: We take xor of all elements. If its non zero then longest subsequence will be the entire array
# and if its zero then it will be one element removed. we only need to guard against the case when all elements of the array are 0
# in which case we should return 0

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        longest = 0
        xor = 0
        
        for right in range(len(nums)):
            xor^=nums[right]
        
        if len(set(nums))==1 and (0 in set(nums)):
            return 0
            
        return len(nums) if xor else len(nums)-1