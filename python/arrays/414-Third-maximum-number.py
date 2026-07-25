# Problem: Leetcode 414 - Third maximum number
# Difficulty: Easy
# Link: https://leetcode.com/problems/third-maximum-number/description/
# Time Complexity: O(n)
# Space Complexity: O(n)  
# Approach: We simply remove the duplicates, sort the list and then if the length is less than 3 we 
# return the max number or otherwise we just return the 3rd biggest number

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums)<3:
            return nums[-1]
        return nums[-3]