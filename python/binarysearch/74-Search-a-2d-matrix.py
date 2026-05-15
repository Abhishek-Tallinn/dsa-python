# Problem: Leetcode 74 - Search in a 2d matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/
# Time Complexity: O(log(m*n)) with m and n being sides of the matrix
# Space Complexity: O(1) as no extra data structure is added
# Approach: we simply flatten the matrix and perform a standard binary search as its sorted.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = [element for row in matrix for element in row]
        l,r = 0,len(flat_matrix)-1
        while l<=r:
            mid = (l+r)//2
            if flat_matrix[mid]==target:
                return True
            elif flat_matrix[mid]>target:
                r = mid-1
            else:
                l = mid+1
            
        return False