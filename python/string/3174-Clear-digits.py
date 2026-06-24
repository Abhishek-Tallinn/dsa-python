# Problem: Leetcode 3174 - Clear digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/clear-digits/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: if a digit is found dont append to stack just pop the stack for an alphabet and if digit is found just append it. The return stack after converting to string


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        '''
        final_s = []
        i=0
        while i < len(s):
            if s[i].isdigit() and i >0:
                while i<len(s) and s[i].isdigit():
                    i+=1
                    final_s.pop() #keep removing alphabets
            if i == len(s):
                break
            final_s.append(s[i])
            i+=1
        if not final_s:
            return ""
        return ''.join(final_s)
        '''
        