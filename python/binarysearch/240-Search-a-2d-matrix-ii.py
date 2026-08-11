# Problem: Leetcode 240 - Search a 2d matrix II
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We iterate through each row and do a binary search on it if it may containg the target

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr):
            left = 0
            right = len(arr)-1
            while left<=right:
                mid = (left+right)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return False
        row_idx = 0
        for row in matrix:
            if row[0] <=target and row[-1]>=target:
                res = search(row)
                if res:
                    return True
        return False