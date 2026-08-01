# Problem: Leetcode 244 - Shortest word distance II
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-word-distance-ii/description/
# Time Complexity: O(n^2)
# Space Complexity: O(n) as we have a hashmap
# Approach: We store indexes of all words in hashmap and then do nested loop over them only for the index of the relevant words which is not purely O(n^2)

from typing import List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = {}
        for i,word in enumerate(wordsDict):
            if word in self.d:
                self.d[word].append(i)
            else:
                self.d[word] = [i]
        

    def shortest(self, word1: str, word2: str) -> int:
        shortest = float('inf')
        first= self.d[word1]
        second = self.d[word2]
        for i in first:
            for j in second:
                shortest = min(shortest,abs(j-i))
        return shortest
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)