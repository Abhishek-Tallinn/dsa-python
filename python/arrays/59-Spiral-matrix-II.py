# Problem: Leetcode 54 - Spiral Matrix II
# Difficulty: Medium
# Link: https://leetcode.com/problems/spiral-matrix-ii/description/
# Time Complexity: O(mxn) - m x n is the size of the matrix as each element is visited once
# Space Complexity: O(1) as no additional data structure is used.
# Approach: Approach is same as usual spiral matrix but with matrix size being initialized with n values and keeping a variable k initialized to 1 and every time k is written to matrix it is incremented by 1.


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = top  = 0
        matrix =[[-1 for _ in range(n)]for _ in range(n)]
        k=1
        right = n-1
        bottom = n-1
        
        
        while left<=right and top<=bottom:
            for col in range(left,right+1):
                matrix[top][col] = k
                k+=1
            top+=1
            for row in range(top,bottom+1):
                matrix[row][right] = k
                k+=1
            right-=1
            if top<=bottom:
                for col in range(right,left-1,-1):
                    matrix[bottom][col] = k
                    k+=1
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1):
                    matrix[row][left] = k
                    k+=1
                left+=1
        return matrix

        