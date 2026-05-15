# Problem: Leetcode 2452 - Words withing two edits of dictionary
# Difficulty: Medium
# Link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/
# Time Complexity: O(n * m * k) where n is the number of words in queries, m is the number of words in dictionary and k is the length of the longest word.
# Space Complexity: O(1)
# Approach: Its more like a brute force approach where we are comparing each word in queries with each word in dictionary and counting the number of edits needed to convert one word to another. If the count is less than or equal to 2, we add the word to the result list else we break immediately from inner loop.


from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for word in queries:
            for d_word in dictionary:
                d_count = 0
                isMatchWithEdit = True
                for c1,c2 in zip(word,d_word):
                    if c1!=c2:
                        d_count+=1
                    if d_count>2:
                        isMatchWithEdit = False
                        break
                if isMatchWithEdit:
                    result.append(word)
                    break
        return result