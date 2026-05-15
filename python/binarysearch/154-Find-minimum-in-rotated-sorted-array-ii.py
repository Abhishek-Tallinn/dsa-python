# Problem: Leetcode 154 - Find minimum in a rotated sorted array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We use binary search but since there is repetition we keep an extra else case in our binary loop 
# where if nums[mid]==nums[r] as mid may itself be the minimum element then we only reduce r by 1 as there are duplicate elements.
# Binary search is about shrinking search space in non ambiguous manner so we use open intervals

from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Main idea is to use binary search for O(log n time)
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid+1
            else: 
                r-=1 #if they are equal then we cannot choose what to do like a typical binary search. so we go slowly
        return nums[l]