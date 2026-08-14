# Problem: Leetcode 844 - Backspace string compare
# Difficulty: Easy
# Link: https://leetcode.com/problems/backspace-string-compare/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we have to use a stack 
# Approach: we add the string to stacks and compare at the end. we pop the stack everytime a # is seen.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2= []

        for char in s:
            if char=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in t:
            if char=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        return stack1 == stack2