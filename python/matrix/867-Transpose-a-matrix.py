# Problem: Leetcode 867 - Transpose a matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/transpose-a-matrix/description/
# Time Complexity: O(mxn) as we traverse the matrix to flip and invert it
# Space Complexity: O(1) as we are modifying the matrix in-place.
# Approach: We can do it manually by creating a new matrix or just use pythonic zip to transpose the matrix

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #manual way
        #must create new matrix if its not a square and copy values
        return [list(row) for row in zip(*matrix)]
        '''
        pythonic way
        return list(zip(*matrix))
        '''
        