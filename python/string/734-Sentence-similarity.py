# Problem: Leetcode 734 - Sentence Similarity
# Difficulty: Easy
# Link: https://leetcode.com/problems/sentence-similarity/description/
# Time Complexity: O(n^2) 
# Space Complexity: O(1)
# Approach: If length of senteces are not same we immediately return False. then we iterate over any sentence and check if values at same index are not equal.
# if they are not then we try to find this unequal pair in similarPairs. If any unequal pair is not found we immediately return False.

from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        for i in range(len(sentence1)):
            found = False
            if sentence1[i] != sentence2[i]:
                if ([sentence1[i],sentence2[i]] in similarPairs ) or \
                ([sentence2[i],sentence1[i]] in similarPairs):
                    found = True
                if not found:
                    return False
        return True