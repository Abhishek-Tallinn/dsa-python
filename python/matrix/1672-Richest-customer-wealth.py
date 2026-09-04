# Problem: Leetcode 1672 - Richest customer wealth
# Difficulty: Easy
# Link: https://leetcode.com/problems/richest-customer-wealth/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We just need to return the max sum from all the rows. so we iterate over rows and keep track of the max sum

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for row in accounts:
            mx = max(mx,sum(row))
        return mx