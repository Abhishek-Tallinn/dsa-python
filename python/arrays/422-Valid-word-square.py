# Problem: Leetcode 422 - Valid word square
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-word-square/description/
# Time Complexity: O(n)
# Space Complexity: O(n)  
# Approach: We split the input words in array and zip each character together. we use zip longest
# otherwise the words where the characters dont exist will be lost as zip by default stops at the shortest iterable
# so with zip longest we will it with empty string. then we return the check that zipped and words should be absolutely equal

from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        zipped = ["".join(chars) for chars in zip_longest(*words, fillvalue='')]
        return zipped == words