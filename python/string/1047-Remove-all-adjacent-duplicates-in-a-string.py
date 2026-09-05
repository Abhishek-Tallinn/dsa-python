# Problem: Leetcode 1047 - Reverse all adjacent duplicated in a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-a-string/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use stack
# Approach: Since we continuously have to pop duplicated stack is the best data structure here.
# every time a new char is same as element at top of the stack we pop it. if not we append current char to stack
# then we return the stack at the end

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)