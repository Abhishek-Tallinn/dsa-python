# Problem: Leetcode 394- Decode string
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-string/description/
# Time Complexity: O(n) as we iterate through the string to add to stack
# Space Complexity: O(n) as we use a stack.
# Approach: We iterate through the string and add elements to stack. every time we hit a bracket we go and resolve the string inside the bracket and add it back to stack. 

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        open_count = 0
        for char in s:
            temp_string = ""
            if char==']':
            
                alphabets = []
                repeat_count = ""
                while stack and stack[-1]!='[':
                    alphabets.append(stack.pop())
                stack.pop()#remove the opening bracket
                while stack and stack[-1].isdigit():
                    repeat_count += stack.pop()
                repeat = int(repeat_count[::-1])
                temp_string = ((''.join(alphabets[::-1])) + temp_string)*repeat
                stack.append(temp_string)
                continue

            stack.append(char)

            
        return ''.join(stack)