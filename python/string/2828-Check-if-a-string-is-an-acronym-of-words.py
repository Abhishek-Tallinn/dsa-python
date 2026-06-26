# Problem: Leetcode 2828 - Check is a string is an acronym of words
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we collect the first chars
# Approach1: we collect the first characters of each word and check its equality with the string.
# Approach2: we can also do it with two pointers where everytime we find the character we increment pointer on s. if pointer reaches the end means it is an acronym.

from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_chars = []
        for word in words:
            first_chars.append(word[0])
        return ''.join(first_chars)==s
        '''
        tracker = 0
        if len(s)< len(words):
            return False
        for word in words:
            if word[0] == s[tracker]:
                tracker+=1
        return tracker==len(s)
        '''