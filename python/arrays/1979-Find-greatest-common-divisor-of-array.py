# Problem: Leetcode 1979 - Find greatest common divisor of array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
# Time Complexity: O(n + n) = O(ns) where n is the length of the array as we sort
# Space Complexity: O(1) 
# Approach: We simply find the mn and max element and calculate the gcd.

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        mn = min(nums)
        mx = max(nums)
        return gcd(mn,mx)