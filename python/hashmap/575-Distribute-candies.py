# Problem: Leetcode 575 - Distribute candies
# Difficulty: Easy
# Link: https://leetcode.com/problems/distribute-candies/description/
# Time Complexity: O(1)
# Space Complexity: O(n) as we use hashmap or set
# Approach: We convert he list to a hashmap or a set and then return the minimum of half length or the types
# of different candies and the minimum of the two is the answer


from collections import Counter
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        return min(len(candyType)//2 , len(types))