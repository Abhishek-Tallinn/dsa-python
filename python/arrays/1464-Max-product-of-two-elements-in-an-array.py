# Problem: Leetcode 1464 - Maximum product of two elements in array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-array/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: Since numbers are positive we just need to find the top two elements and subtract one 
# from each and multiply and return the result

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)