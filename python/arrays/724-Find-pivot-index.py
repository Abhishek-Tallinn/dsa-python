# Problem: Leetcode 724 - Find Pivot Index
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-pivot-index/description/
# Time Complexity: O(n) as we iterate through the array once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We calculate total sum of array and for each index iterate over the array and check if the running sum is equal to balance - current elemenet
# which will basically give us the suffix sum. If we find such an index we return it else we return -1

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        s=0
        for i in range(len(nums)):
            if s == (total - s - nums[i]):
                return i     
            s+=nums[i]
        
        return -1