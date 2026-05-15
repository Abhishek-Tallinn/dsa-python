# Problem: Leetcode 153 - Find minimum in a rotated sorted array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We binary search and the inflection points is that if num[mid]<nums[-1] as array is sorted then this could be the minimum element. 
# So we take it into our target index and make right = mid-1 and continue the search leftward.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        l,r = 0 , len(nums) - 1
        target_index = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < nums[-1]:
                target_index = mid
                r = mid-1
            else:
                l = mid+1
            #this time we dont need else statement as there is no duplication
        return nums[target_index]
        '''
        l,r = 0 , len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]
        '''