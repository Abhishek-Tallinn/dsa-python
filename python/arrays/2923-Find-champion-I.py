# Problem: Leetcode 2923 - Find champion I
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-champion-i/description/
# Time Complexity: O(n^2) in worse case
# Space Complexity: O(1)
# Approach: We need insight that the strongest team will have all 1s except itself. So we iterate over each team
# and find the one which has ones count equal to length of grid -1 and return its index.
from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i,team in enumerate(grid):
            if team.count(1) == len(grid)-1:
                return i