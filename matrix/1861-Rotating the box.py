# Problem: Leetcode 1861 - Rotate the box
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotating-the-box/description/
# Time Complexity: O(mxn) where mxn is the size of the matrix.
# Space Complexity: O(mxn) as we make a new rotated matrix
# Approach: We rotate the matrix and then we scan each column to find the empty spaces. As we go up from bottom of column since we are simulating gravity we keep an empty count of empty spaces seen so far.
# if we hit a block we reset the empty spaces and if we hit a strong we swap it with the total empty spaces we have to far. since its a swap we dont add to empty space count when swapping.
# Approach2: You can do it in O(1) space by simulating gravity and using position based substitution rather than keeping a count of empty cells and moving the rock that many cells


from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #first i rotate 90 clockwise
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        if rows == 1 and cols==1:
            return boxGrid
        rotated = [list(row) for row in list(zip(*boxGrid[::-1]))]
        rows,cols = cols,rows
        
        for i in range(cols):
            j = rows-1
            e_count=0
            while j >= 0:
                while j>=0 and rotated[j][i]==".":
                    e_count+=1
                    j-=1
                if j <0:
                    break
                if rotated[j][i] == "*":
                    e_count = 0
                elif rotated[j][i] == "#":
                    rotated[j][i],rotated[j+e_count][i] = rotated[j+e_count][i],rotated[j][i]
                j-=1
                
        return rotated