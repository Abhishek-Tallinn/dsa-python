# Problem: Leetcode 2154 - Keep multiplying found values by 2
# Difficulty: Easy
# Link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
# Time Complexity: O(n) as max we would have to check all the elements in it or less
# Space Complexity: O(1) as no extra data structure is used
# Approach: 

from typing import List
from collections import Counter

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d = Counter(nums)
        while original in d:
            original*=2
        return original