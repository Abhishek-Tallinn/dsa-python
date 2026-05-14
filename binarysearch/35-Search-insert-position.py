# Problem: Leetcode 35 - Search Insert position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: we do a usual binary search to find the target. however, every time a target is not found we maintain index variable to find the possible insert position of our target element.
# if nums[mid] is greater than target then target will take the place of mid and is nums[mid] is less than target then target will take place of mid-1.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        index = 0
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        # now we do binary search
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
                index = mid
            else:
                left=mid+1
                index = mid+1
        
        return index