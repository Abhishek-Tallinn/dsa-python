# Problem: Leetcode 852 - Peak Index in a Mountain Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We shrink the search space as per the slope found at mid. but to avoid wrap around indexing where in case mid is 0
# then mid get compared with last element of array we shrink the space conservatively by setting right = mid instead of mid-1.
# if we want to use mid-1 we will have to use boundary checks then

from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1