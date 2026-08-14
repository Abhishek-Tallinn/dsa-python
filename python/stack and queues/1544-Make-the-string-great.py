# Problem: Leetcode 1544 - Make the string great
# Difficulty: Easy
# Link: https://leetcode.com/problems/make-the-string-great/description/
# Time Complexity: O(n) as we only append and pop to stack
# Space Complexity: O(n) as we have to use a stack
# Approach: We keeping adding characters to the stack but we pop the stack if a bad combination is found. and if we pop then in 
# that case we dont append to the stack.


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and ((c.isupper() and stack[-1] == c.lower()) or (stack[-1].isupper() and stack[-1].lower()==c)):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)