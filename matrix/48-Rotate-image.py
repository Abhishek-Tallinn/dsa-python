# Problem: Leetcode 48 - Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/description/
# Time Complexity: O(n^2) where n is the size of the matrix.
# Space Complexity: O(1) as we are modifying the matrix in-place.
# Approach: As the question asks for 90 degree clockwise rotation we transpose the matrix(swap across diagnol) and then we switch the reverse the rows which is the standard way to rotate clockwise.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for row in matrix:
            row.reverse()