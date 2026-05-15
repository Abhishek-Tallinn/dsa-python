# Problem: Leetcode 73 - Set matrix zeroes
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/description/
# Time Complexity: O(mxn) as we traverse the matrix to find target rows and cols
# Space Complexity: O(1) as we are modifying the matrix in-place.
# Approach: We iterate the matrix and find the position of original zeros and then set the target rows and target cols as zeroes.
# the modification is in place and no extra data structure is created.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        target_rows = set()
        target_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    target_rows.add(i)
                    target_cols.add(j)
        for row in list(target_rows):
            matrix[row] = [0]*len(matrix[0])
        for col in list(target_cols):
            #set each column to 0
            for row in range(len(matrix)):
                matrix[row][col] = 0
        return matrix
        