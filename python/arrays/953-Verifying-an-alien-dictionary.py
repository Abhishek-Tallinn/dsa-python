# Problem: Leetcode 953 - Verifying an alien dictionary
# Difficulty: Easy
# Link: https://leetcode.com/problems/verifying-an-alien-dictionary/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: We make a dictionary of alient order mapping each character to an index
# then we run over words and convert each one with the previous one with our lex function
# that check if string are lexicographically sorted

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {char:idx for idx,char in enumerate(order)}
        def lex(s1,s2):
            for i in range(min(len(s1),len(s2))):
                if d[s1[i]]!=d[s2[i]]:
                    return d[s1[i]] < d[s2[i]]
                #if d[s1[i]] < d[s2[i]]:
                #    return True
                #elif d[s1[i]] > d[s2[i]]:
                #    return False
                #else:
                #    continue
            return len(s1) <= len(s2)
        for i in range(1,len(words)):
            if not lex(words[i-1],words[i]):
                return False
        return True