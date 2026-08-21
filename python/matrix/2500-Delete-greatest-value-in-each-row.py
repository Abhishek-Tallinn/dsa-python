# Problem: Leetcode 2500 - Delete greatest value in each row
# Difficulty: Easy
# Link: https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
# Time Complexity: O(mxn) where mxn is the size of the matrix.
# Space Complexity: O(mxn) as we make a new rotated matrix
# Approach1: we use smart appraoch of sorting each row and then we can keep taking max value of each column while iterating from last column to the first 
# and we keep adding them to the ans
# Approach2: We do it traditional way without sorting but that means we need to track all the removed cells and 
# then skip then in each iteration and its also O(n^2)

from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        ans = 0
        for col in range(len(grid[0])-1,-1,-1):
            mx = 0
            for row in range(len(grid)):
                mx = max(mx,grid[row][col])
            ans+=mx
        return ans
                
        '''
        full solve
        removed_cells = set()
        total = len(grid)*len(grid[0])
        cnt = 0
        ans = 0
        while cnt<total:
            g_mx = 0
            for i in range(len(grid)):
                mx = 0
                target_idx = -1
                for j in range(len(grid[0])):
                    if (i,j) in removed_cells:
                        continue
                    if grid[i][j] >= mx:
                        mx = grid[i][j]
                        target_idx = j
                removed_cells.add((i,target_idx))
                cnt+=1
                g_mx = max(g_mx,mx)
            ans += g_mx
        return ans
        '''