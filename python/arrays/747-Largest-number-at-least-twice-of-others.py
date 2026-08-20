# Problem: Leetcode 747 - Largest number at least twice of others
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach1: is O(n) and O(1) where we keep track of two two elements and index of the max elements and return it if required.
# Approach2: We can sort the list and compare the last two elements and then if last elements is twice or greater than second last 
# then we can return the index of the last element.
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        one = 0
        two = 0
        mx_index = 0
        for i,num in enumerate(nums):
            if num > one:
                two = one
                one = num
                mx_index = i
            elif num < one and num > two:
                two = num
         
        #temp = sorted(nums)
        #if temp[-1] >= 2*temp[-2]:
        #    return nums.index(temp[-1])
        if one>=2*two:
            return mx_index
        return -1