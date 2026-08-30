# Problem: Leetcode 2114 - Maximum number of words found in sentences
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We simply take each sentence and split it and update our max counter

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for sentence in sentences:
            mx = max(mx,len(sentence.split()))
        return mx