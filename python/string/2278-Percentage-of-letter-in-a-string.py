# Problem: Leetcode 2278 - Percentage of letter in a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/percentage-of-letter-in-a-string/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We count the occurences and return the percentage value.

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = sum(1 for char in s if char==letter)
        return cnt*100//len(s)