# Problem: Leetcode 3513 - Number of unique XOR triplets I
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Its a math pattern since unique xor triplet values will depend on the the length of input array. so we keep reducing the length
# by a factor of 2 in the a while loop to find max power of 2 as a number that exists. then the total values possible will be twice of that number
# so we multipl 2**max_power with 2 and return answer

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        n = len(nums)
        mx_pow2 = 0
        while n>0:
            mx_pow2+=1
            n = n//2
        
        return 2*(2**(mx_pow2-1))