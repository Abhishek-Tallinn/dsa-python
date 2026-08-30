# Problem: Leetcode 2108 - Find first palindromic string in the array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply check each string in word for palindrome and return. If return is not triggered in loop we return ""

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word==word[::-1]:
                return word
        return ""