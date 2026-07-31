# Problem: Leetcode 463- Island perimeter
# Difficulty: Easy
# Link: https://leetcode.com/problems/island-perimeter/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We iterate through matrix and everytime we find a land piece we pass it to the checkNeighbour function
# and this piece contribution to the perimeter will be as per the amount of neighbours it has 

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def checkNeighbour(grid,r,c):
            nei = 0
            if r > 0 and grid[r-1][c] == 1:
                 nei+=1
            if r<len(grid)-1 and grid[r+1][c] == 1:
                nei+=1
            if c>0 and grid[r][c-1] == 1:
                nei+=1
            if c<len(grid[0])-1 and grid[r][c+1] == 1:
                nei+=1
            return 4-nei
        peri = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    peri+=checkNeighbour(grid,row,col)
        return peri