# Problem: Leetcode 1762 - Buildings with an ocean view
# Difficulty: Easy
# Link: https://leetcode.com/problems/buildings-with-an-ocean-view/description/
# Time Complexity: O(n) as we loop over the array heights
# Space Complexity: O(n) as we use a stack
# Approach: We iterate backwards over builds and keep popping stack if current height is great than all the heights in stack
# if whole stack is popped means current builds has view of the ocean and we check that if not stack then we append it to the ans.
# Then we append current height index in stack and continue

from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
            if not stack:
                ans.append(i)
            stack.append(i)
        return ans[::-1]