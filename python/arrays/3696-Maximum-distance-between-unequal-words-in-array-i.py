# Problem: Leetcode 3696 - Maximum distance between unequal words in array I
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/description/
# Time Complexity: O(n^2) as its allowed by the constraints
# Space Complexity: O(1) 
# Approach: Since input is small we just use a nested loop to check each element and cal max distance between unequal elements

from typing import List

class Solution:
    def maxDistance(self, words: List[str]) -> int:
        mx_dist = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j]:
                    continue
                mx_dist = max(mx_dist, j-i+1)
                if mx_dist == len(words):
                    break
        return mx_dist