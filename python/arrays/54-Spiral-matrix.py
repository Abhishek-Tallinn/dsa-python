# Problem: Leetcode 54 - Spiral Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/spiral-matrix/description/
# Time Complexity: O(mxn) - m x n is the size of the matrix as each element is visited once
# Space Complexity: O(1) as no additional data structure is used.
# Approach: We iterate through the elements keeping walls on each side i.e top,right,bottom and left and the walls are moved inwards after each for loop is finished. 
# the overall movement is controlled by a master why loop which checks for range.

# Solution2 - It a with traversal using two pointers instead of utilizing entire row and column. It has same time and space complexity but it less elegant.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        flat_spiral = []
        left = top = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        while left<=right and top<=bottom:
            #take first row
            for col in range(left,right+1):
                flat_spiral.append(matrix[top][col])
            top+=1

            #then take right column
            for row in range(top,bottom+1):
                flat_spiral.append(matrix[row][right])
            right-=1

            #now we check to ensure its not already ended
            if top<=bottom:
                for col in range(right,left-1,-1):
                    flat_spiral.append(matrix[bottom][col])
                bottom-=1

            if left<=right:
                for row in range(bottom, top-1,-1):
                    flat_spiral.append(matrix[row][left])
                left+=1

        return flat_spiral

        '''
        flat_spiral = []
        left = top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        i=j=0
        while left<=right and top<=bottom:
            
            for row in range(top,top+1):
                for col in range(left,right+1):
                    flat_spiral.append(matrix[row][col])
                
            top+=1
            if len(flat_spiral) == len(matrix)*len(matrix[0]):
                return flat_spiral
            
            for row in range(top,bottom+1):
                for col in range(right,right+1):
                    flat_spiral.append(matrix[row][col])

            right-=1
            
            for row in range(bottom,bottom-1,-1):
                for col in range(right,left-1,-1):
                    flat_spiral.append(matrix[row][col])
            bottom-=1
            if len(flat_spiral) == len(matrix)*len(matrix[0]):
                return flat_spiral
            
            for row in range(bottom,top-1,-1):
                for col in range(left,left+1):
                    flat_spiral.append(matrix[row][col])
            left+=1         
        return flat_spiral
        '''



            

        