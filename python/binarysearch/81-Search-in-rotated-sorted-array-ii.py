# Problem: Leetcode 33 - Search in a rotated sorted array-ii
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-a-rotated-sorted-array-ii/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: It is same as search in rotated sorted array-i but with duplicate elements. So we introduce a check which says that 
# if all left,mid and nums come out to be equal then we shring both left and right and continue the loop. This is to avoid cases of maximum duplicaty.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            elif nums[left]<=nums[mid]: #means left part is sorted
                if nums[left]<=target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
                  
        return False