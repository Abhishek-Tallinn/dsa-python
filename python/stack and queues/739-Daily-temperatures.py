# Problem: Leetcode 739 - Daily temperatures
# Difficulty: Medium
# Link: https://leetcode.com/problems/daily-temperatures/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we have to use a stack 
# Approach1: We keep indices in stack instead of values and populate the answer array with 0 to have default values anyway.
# then we iterate the array and we keep poppping indices till  the temperature in stack is less than or equal to current temperatures.
# if stack is empty we continue but if not then we write the difference between index at the top of the stack and current index in the answer array
# which will determine the difference between next higher temperature.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans