# Problem: Leetcode 747 - Toeplitz matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/toeplitz-matrix/description/
# Time Complexity: O(n^2) 
# Space Complexity: O(n) as we make a hashmap
# Approach: We put diagonals into a hashmap so we can group diagonal values as per hashmap keys and then check if they have same element
from collections import defaultdict
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diags2 = []
        diags = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diags[i-j].append(matrix[i][j])
        return all(len(set(d))==1 for d in diags.values())