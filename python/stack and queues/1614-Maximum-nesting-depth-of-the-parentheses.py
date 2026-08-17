# Problem: Leetcode 1614 - Maximum nesting depth of the parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
# Time Complexity: O(n) as we loop over the string
# Space Complexity: O(n) as we have to use a stack
# Approach: We add to stack everytime we find an opening bracked and take hte length of stack in mx variable and when closing bracket is found we pop from stack.

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        mx = 0
        for c in s:
            if c == '(':
                stack.append(c)
                mx = max(mx,len(stack))
            elif c==')':
                stack.pop()
        return mx