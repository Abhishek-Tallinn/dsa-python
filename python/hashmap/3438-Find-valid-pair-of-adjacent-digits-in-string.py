# Problem: Leetcode 3438 - Find valid pair of adjacent digits in string
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-valid-pairs-of-adjacent-digits-in-string/description/
# Time Complexity: O(n) as we go through the array once
# Space Complexity: O(1). we make dictionary but it has fixed length
# Approach1: we simply check each element and its next element that they are not equal and then check their freq from hashamp and return string if all conditions are true.
from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        d = Counter(s)
        for i in range(len(s)-1):
            if s[i]!=s[i+1] and d[s[i]] == int(s[i]) and d[s[i+1]] == int(s[i+1]):
                return s[i]+s[i+1]
        return ""