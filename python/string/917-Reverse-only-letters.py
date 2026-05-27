# Problem: Leetcode 917 - Reverse Only Letters
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-only-letters/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(n) as we make a list and join it back
# Approach: We extract the alphabest out of the list and then we iterating on the string and build the result list. if char in string if alphabet we instead
# append the last element of alphabet list and move our pointer backwards. We could also do it with stack and pop this element. 
# Approach2 - O(1) space approach is using two pointers and swapping when both pointers point to characters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = []
        for char in s:
            if char.isalpha():
                alpha.append(char)
        res = []
        j = len(alpha)-1
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(alpha[j])
                j-=1
            else:
                res.append(s[i])

        return ''.join(res)
            
        '''
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)
        '''