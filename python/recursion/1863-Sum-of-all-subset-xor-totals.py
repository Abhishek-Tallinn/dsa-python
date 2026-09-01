# Problem: Leetcode 1863 - Sum of All Subset XOR Totals
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
# Time Complexity: O(2^n) where n is the length of the array as we generate all subsets.
# Space Complexity: O(n) for the recursion stack
# Approach: We use recursion to generate all possible subsets as that is the only way to know xor values
# but to avoid overhead we dont store any of them and just take their total xor value saving memory. Since length is max 12
# we can generate all 2^12 subsets and take their xor value and return the total sum of all xor values.

from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def find_subsets(start,curr_set):
            xor = 0
            for element in curr_set:
                xor^=element
            result = xor
            for i in range(start,len(nums)):
                curr_set.append(nums[i])
                result+=find_subsets(i+1,curr_set)
                curr_set.pop()
            return result
        return find_subsets(0,[])