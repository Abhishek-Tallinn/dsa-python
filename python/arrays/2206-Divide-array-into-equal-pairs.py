# Problem: Leetcode 2206 - Divide array into equal pairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/divide-array-into-equal-pairs/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We make a hashmap and check if any key has odd values meaning it cannot be part of both pairs and we return False immediately
# if loop ends we return True
from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for value in d.values():
            if value%2==1:
                return False
        return True