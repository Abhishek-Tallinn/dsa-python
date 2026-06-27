# Problem: Leetcode 2696 - Minimum string length after removing substrings
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a stack
# Approach: We iterate over the string and add elements to stack. however if the current char is B or D then they can possibly complete a substring AB or CD which we need to drop
# so if char is B or D we check if the last element of stack i.e stack[-1] is A for B or C for D. if it is then we pop the stack and dont append the current character to it.
# then we return the length of string.



class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if (char=="B" and stack and stack[-1]=="A") or (char=="D" and stack and stack[-1]=="C"):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)