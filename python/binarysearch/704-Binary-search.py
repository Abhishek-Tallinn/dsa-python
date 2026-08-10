# Problem: Leetcode 704 - Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: Simple binary search over the array where its already sorted

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1