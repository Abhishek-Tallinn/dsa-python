# Problem: Leetcode 256 - Paint houses
# Difficulty: Medium
# Link: https://leetcode.com/problems/paint-houses/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only keep last state
# Approach: This is dp problem as we need to evaluate all paths to eventually find the minimal value.
# the best path is not acheived by making greedy solution.

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_red = prev_blue = prev_green = 0
        for cost_red,cost_blue,cost_green in costs:
            curr_red = min(prev_blue,prev_green) + cost_red
            curr_blue = min(prev_red,prev_green) + cost_blue
            curr_green = min(prev_red,prev_blue) + cost_green
            prev_red = curr_red
            prev_blue = curr_blue
            prev_green = curr_green
        return min(prev_red,prev_blue,prev_green)