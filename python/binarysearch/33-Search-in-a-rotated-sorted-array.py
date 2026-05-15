# Problem: Leetcode 33 - Search in a rotated sorted array
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-a-rotated-sorted-array/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: we do a usual binary search to find the target. HOwever, if mid is not target , then we have to determine which side of mid is sorted and 
# continue the search in that part accordingly. this we acheive by explicity checking target with nums[mid] and nums[left] or nums[right].

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left]<=nums[mid]:
                if nums[left]<=target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            
                  
        return -1