# Problem: Leetcode 2784 - Check if array is good
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-array-is-good/description/
# Time Complexity: O(nlogn ) - as we go through all the element of from 1 to max and we are also sorting the list
# Space Complexity: O(n) as we make a new sorted list
# Approach1: we simply  sorted the list and compare it to a generated list in the range 1 to n+1 with an extra n value
# Approach2: we can make a hashmap of the values and then in range 1 to n check that all key values are exactly 1 and check key value of n to be 2 separately.

from collections import Counter
from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n= max(nums)
        return sorted(nums) == list(range(1, n + 1)) + [n]
        '''
        freq_map = Counter(nums)
        n = max(nums)
        if freq_map[n]!=2:
            return False
        for i in range(1,n):
            if i not in freq_map or freq_map[i]!=1:
                return False
        return True
        '''
       