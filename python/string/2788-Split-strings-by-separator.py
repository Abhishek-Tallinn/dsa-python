# Problem: Leetcode 2788 - Split string by separator
# Difficulty: Easy
# Link: https://leetcode.com/problems/split-string-by-separator/description/
# Time Complexity: O(n) - passing over each word in array
# Space Complexity: O(n) as we construct res array.
# Approach: we iterate over each word and we split it across separator and extend the ans array. then we iterate over ans to remove the empty string.

from typing import List;

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            temp = word.split(separator)
            ans.extend(temp)
        res = [word for word in ans if word!='']
        return res