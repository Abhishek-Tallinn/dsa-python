# Problem: Leetcode 861 - Score after flipping matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/score-after-flipping-matrix/description/
# Time Complexity: O(mxn) as we traverse the matrix to flip and invert it
# Space Complexity: O(1) as we are modifying the matrix in-place. the indices set has a max value of only 20.
# Approach: We iterate over the matrix and if the first element of each row is 1 we continue as we cannot increase that number anymore.
# if not then we flip as flipping will always make the number bigger. then we iterate over columns leaving the first column which one has ones.
# for column we decide based on count of 1s. if 1s are in minority then flipping it would be advantage for us.
# for first we take the indices of columns which have 1 in minority and then in second iteration over columns we flip these bits.
# then we iterate last time over matrix and take each value and sum them.

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            if grid[i][0]==1:
                continue
            else:
                for j in range(len(grid[i])):
                    grid[i][j]^=1
        indices = set()
        for i in range(1,len(grid[0])):
            cnt = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    cnt+=1
            if cnt<(len(grid)/2):
                indices.add(i)
        for i in range(1,len(grid[0])):
            if i in indices:
                for j in range(len(grid)):
                    grid[j][i]^=1
            else:
                continue
                

        for row in grid:
            s = 0
            power = 0
            for bit in row[::-1]:
                s+=bit*(2**power)
                power+=1
            total+=s
        return total