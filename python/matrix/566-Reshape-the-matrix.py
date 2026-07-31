# Problem: Leetcode 566 - Reshape the matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/reshape-the-matrix/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we contruct the matrix to return
# Approach: We flatten the matrix and then allocate the values to result matrix. if the length of flat 
# matrix is not equal to the total r*c then that means the shape is a mismatch so we return the usual matrix

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [e for row in mat for e in row]
        if len(flat)!=r*c:
            return mat
        result = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = flat[k]
                k+=1
        return result