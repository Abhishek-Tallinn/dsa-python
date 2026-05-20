# Problem: Leetcode 3011 - Find if Array Can Be Sorted
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-if-array-can-be-sorted/description/
# Time Complexity: O(n^2) - as we go through the array twice
# Space Complexity: O(n) as no additional data structure is used.
# Approach: We just iterate through each element as its allowed by the constraints and check that if there are any two elements that are not sorted 
# relative to each other and have different number of set bits then we return false. If we do not find any such pair then we return true.
# Appraoch 2: we can use appoach with hashmap where we group number by their bit_count() in a hasmap and sorted the numbers within their group
# then we rebuild the array from hashmap and check it against the sorted original array. If its equal we can return true. 
# The second approach achieved O(n log n) time complexity but space complexity will be same.

from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums==sorted(nums):
            return True
        bits = [x.bit_count() for x in nums]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j] and bits[i]!=bits[j]:
                        return False
                    
        
        return True