# Problem: Leetcode 1967 - Number of strings that appear as substrings in word
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-words/description/
# Time Complexity: O(n^2) as we do a naive substring check
# Space Complexity: O(1) 
# Approach: Since iterate through each pattern and check if its in word using the naive 'in' operator in python.
# and we keep increment count if it is found. then we return cnt.

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for s in patterns:
            if s in word:
                cnt+=1
        return cnt