# Problem: Leetcode 2965 - Find missing and repeated values
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-missing-and-repeated-values/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a count array
# Approach: We make a count array for number from 1 to n^2 to the length of the count array is (n^2+1). Then we iterate
# the matrix and increment the index of the number each time we see it. Then for number from 1 to n^2 the number whose index is 2 is repeated and 
# number whose index is 0 is missing and we return them.

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = repeating = -1
        n = len(grid)
        count_array = [0]*(n*n+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count_array[grid[i][j]]+=1
        for i in range(1,len(count_array)):
            if count_array[i] == 2:
                repeated = i
            if count_array[i]==0:
                missing = i
        return [repeated,missing]