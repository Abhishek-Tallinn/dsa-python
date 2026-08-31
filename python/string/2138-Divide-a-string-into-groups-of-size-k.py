# Problem: Leetcode 2138 - Divide a string into groups of size K
# Difficulty: Easy
# Link: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(k) where k is the number of words in title that are sliced
# Approach:  we simply keep appending substring of len(k) and at the end if length of substring
# is less than k then we just fill the remaining length with characters and append it too.

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0,len(s),k):
            sub = s[i:i+k]
            if len(sub)<k:
                sub+=fill*(k-len(sub))
            ans.append(sub)
        return ans