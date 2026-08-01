# Problem: Leetcode 84 - Largest Rectangle in Histogram
# Difficulty: Hard
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# Time Complexity: O(n) as we iterate through the histogram elements
# Space Complexity: O(n) as we use a stack to push and pop elements
# Approach: Use a stack to keep track of indices of histogram bars in increasing order of their heights. For each bar, calculate the area with the bar as the smallest one and update the maximum area.
# after the iteration is done we check the leftover values in stack and keep calculating the max width and 
# consequently the max rectangle area that we can have.


from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx_area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                height = heights[idx]
                width = i - (stack[-1]+1 if stack else 0)
                area = height*width
                mx_area = max(mx_area, area)
            stack.append(i)
        print(stack)
        while stack:
            idx = stack.pop()
            h = heights[idx]
            width = len(heights) - (stack[-1]+1 if stack else 0)
            
            mx_area = max(mx_area, h*width)
        return mx_area