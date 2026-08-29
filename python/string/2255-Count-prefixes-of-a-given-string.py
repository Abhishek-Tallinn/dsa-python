# Problem: Leetcode 2255 - Count prefix of a given string
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
# Time Complexity: O(n) but can be O(n^2) in worst case
# Space Complexity: O(1) 
# Approach: We take each word and slice the string upto its length and compare if they are equal.
# if yes then we increment counter

from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for word in words:
            n = len(word)
            if s[:n] == word:
                cnt+=1
        return cnt
        