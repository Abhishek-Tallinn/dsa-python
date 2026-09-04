# Problem: Leetcode 1662 - Check if two string arrays are equivalent
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
# Time Complexity: O(n) as we perform join operations
# Space Complexity: O(n) as we make a string
# Approach: We simply concatenate the array element to make a final string to compare equality. We do this in one line
# by using the join operation
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)