# Problem: Leetcode 172 - Factorial Trailing Zeros
# Difficulty: Medium
# Link: https://leetcode.com/problems/factorial-trailing-zeros/description/
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Count the number of 5s as a prime factor in n factorial as the factors of 2 are abundant and can always be combined iwht 5 
# to produce a zero in the unit digit. 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        power = 5
        total = 0
        while power <= n:
            total+=n//power
            power = power*5
        
        return total