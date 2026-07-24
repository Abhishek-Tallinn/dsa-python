# Problem: Leetcode 3706 - Maximum distance between unequal words in array II
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: Since we have to find unequal elements we simply compare each element with the two ends 
# and keep track of the max distance which will calculate the max distance.

from typing import List

class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        first = words[0]
        last = words[-1]
        mx_dist = 0
        for i in range(1,len(words)):
            if words[i]!=first:
                mx_dist = max(mx_dist,i+1)
            if words[i]!=last:
                mx_dist = max(mx_dist,n-i)
        return mx_dist