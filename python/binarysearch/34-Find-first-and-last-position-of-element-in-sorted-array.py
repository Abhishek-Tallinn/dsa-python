# Problem: Leetcode 34 - Find first and last position of element in sorted array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: Usual binary search to find the target element. We main the flag to see if it is found or not. if found we run two while loops
# to set the start and end pointers. If found flag is not set then we just return [-1,-1]

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = False
        start = end = 0
        left,right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                found = True
                start,end = mid,mid
                while start>0 and nums[start] == nums[start-1]:
                    start-=1
                while end+1 < len(nums) and nums[end] == nums[end+1]:
                    end +=1
                break
    
            elif nums[mid]> target:
                right = mid-1
            else:
                left = mid+1

        if not found:
            return [-1,-1]
        
        return [start,end]