# Problem: Leetcode 976 - Largest perimeter triangle
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-perimeter-triangle/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach 1- We simply check 3 adjacent starting from back as checking any two lower values with the largest element cannot work 
# because nums is sorted. So we have to keep our biggest side in range and if the two closest values on its left cannot exceed the largest values and no values further left will exceed it.
# So therefore we keep going leftwards in pairs of 3 and checking if two sides sum exceeds the third side 
# which is rule for making a triangle.

from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        last = len(nums)-1
        for i in range(len(nums)-2,0,-1):
            if nums[i]+nums[i-1] > nums[i+1]:
                return nums[i] + nums[i-1] + nums[i+1]
        return 0