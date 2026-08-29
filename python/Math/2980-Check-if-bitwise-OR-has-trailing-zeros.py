# Problem: Leetcode 2980 - Check if bitwise OR has trailing zeros
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-bitwise-OR-has-trailing-zeros/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We take a bitwise OR of each element but since OR will make the last bit 1 in either case if any of the number being in OR operations 
# has a 1 in the LSB place, hence we need to have two or more elements who have 0 in the LSB place as thats the only 
# way to keep 0 in LSB by choosing two or more element. So we loop the array and make a count.
# and then we check if we did find two numbers or not.

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for num in nums:
            if not num&1:
                cnt+=1
        return cnt>=2