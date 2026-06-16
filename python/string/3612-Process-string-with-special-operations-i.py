# Problem: Leetcode 3612 - Process String with Special Operations I
# Difficulty: Medium
# Link: https://leetcode.com/problems/process-string-with-special-operations-i/description/
# Time Complexity: O(n+k) as we loop through the strip and O(k) as we extend the resulting list
# Space Complexity: O(n) as we we make another list and extension and reversal is in place
# Approach: We just iterate through the string and perform the resulting operations and add characters to a list as we dont have to make a new string every time 
# which is immutable. 


class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            if char.isalpha():
                res.append(char)
            elif char=='*':
                if res:
                    res.pop()
            elif char=='#':
                res.extend(res)
            elif char=='%':
                res.reverse()
        return ''.join(res)