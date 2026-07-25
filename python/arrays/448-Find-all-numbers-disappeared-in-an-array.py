# Problem: Leetcode 448 - Find all numbers disappeared in an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-all-numbers-disppeared-in-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n)  
# Approach: We iterate from 1 to n and we do look up in the set and see which element is missing.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums)
        ans = [i for i in range(1,n+1) if i not in s ]
        return ans