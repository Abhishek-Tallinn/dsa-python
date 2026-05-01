# Problem: Leetcode 78 - Subsets
# Difficulty: Medium
# Link: https://leetcode.com/problems/subsets/description/
# Time Complexity: O(n*2^n) where n is the number of elements in the input array and subsets would be 2 to power n
# Space Complexity: O(2^n) for storing all subsets.
# Approach: Use backtracking to generate all possible subsets.
# At each step i am adding the next element to current set and appending current set to subsets. 
# The backtracking function is called recursively with next index and current set. After the recursive call, we pop the last element to backtrack and explore other possibilities.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        def backtrack(index,currset):
            subsets.append(currset[:])
            for i in range(index, n):
                currset.append(nums[i])
                backtrack(i+1,currset)
                currset.pop()
        backtrack(0,[])

        return subsets