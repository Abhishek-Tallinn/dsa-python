# Problem: Leetcode 1290 - Shift 2D grid
# Difficulty: Easy
# Link: https://leetcode.com/problems/shift-2D-grid/description/
# Time Complexity: O(n) as we traverse the matrix to flatten and rotate it
# Space Complexity: O(n) as we make a flat matrix
# Approach: We flatten the matrix, apply the normalized rotation and then make it back into grid
# and return the grid

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid
        flat_grid = [num for row in grid for num in row]
        if k%len(flat_grid) == 0:
            return grid
        k = k%len(flat_grid)
        shifted_grid = flat_grid[-k:] + flat_grid[:-k]
        ans = [[-1]*len(grid[0]) for _ in range(len(grid))]
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[i][j] = shifted_grid[counter]
                counter+=1
        return ans