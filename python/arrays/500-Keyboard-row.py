# Problem: Leetcode 500 - Keyboard Row
# Difficulty: Easy
# Link: https://leetcode.com/problems/keyboard-row/description/
# Time Complexity: O(n) where n is the total length of words and each character is looked up in a small set of alphabets which is O(1) effectively
# Space Complexity: Sets are small size so little space is taken. O(26)
# Approach: We simply convert each keyboard row into set for quick look up. then we check all characters of each word in words and if all characters are member of any one of the set,
# that means that word is in one row so we append it to our answer and return it. we use all function to make if pythonic.

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        res = []
        for word in words:
            lword = word.lower()
            if all(char in first for char in lword) or all(char in second for char in lword) or all(char in third for char in lword):
                res.append(word)
        return res
