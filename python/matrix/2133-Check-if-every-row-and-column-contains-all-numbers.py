# Problem: Leetcode 2133 - Check if every row and column contains all numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/
# Time Complexity: O(n) as we loop rings once and then memo once
# Space Complexity: O(n) as we use memo hashmap
# Approach: We iterate over all rows and column if the set - meaning we remove repetitions has length of n meaning it has all numbers from 1 to n

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        s = n*(n+1)//2
        for row in matrix:
            if len(set(row))!=n:
                return False
        for col in zip(*matrix):
            if len(set(col))!=n:
                return False
        return True