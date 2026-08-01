# Problem: Leetcode 245 - Shortest word distance III
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-word-distance-iii/description/
# Time Complexity: O(n
# Space Complexity: O(n) as we have a hashmap
# Approach: We iterate throught the array and keep track of the last indices seen for the two words and keep calculating the distanceo the fly to
# keep a track of it. if both words are same we make a special branch where we keep switching the curr index seen and calculating distance and then putting it into the prev index
# as both indices belong to same work but they are diff in the list

from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_latest = float('inf')
        word2_latest = float('inf')
        shortest = float('inf')
        if word1==word2:
            for i, word in enumerate(wordsDict):
                if word == word1:
                    word1_latest = word2_latest
                    word2_latest = i       
                shortest = min(shortest, abs(word1_latest-word2_latest))
            return shortest

        for i,word in enumerate(wordsDict):
            if word == word1:
                word1_latest = i
            if word==word2:
                word2_latest = i
            shortest = min(shortest,abs(word1_latest-word2_latest))
        return shortest