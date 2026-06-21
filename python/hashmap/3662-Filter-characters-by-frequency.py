# Problem: Leetcode 3662 - Filter characters by frequency
# Difficulty: Easy
# Link: https://leetcode.com/problems/filter-characters-by-freq/description/
# Time Complexity: O(n) as we iterate over the string
# Space Complexity: O(n) as we make a hasmap
# Approach: We simply make a hashmap and then iterate over original string and check which characters have freq < k and collect them in correct order.

from collections import Counter
class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        d = Counter(s)
        res = []
        for char in s:
            if d[char]<k:
                res.append(char)
        return ''.join(res)