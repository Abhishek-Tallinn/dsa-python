# Problem: Leetcode 2521 - Distinct prime factors of product of array
# Difficulty: Easy
# Link: https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Since we have to calculate DISTINCT prime factors of product of all numbers,
# its smarter to just calculate the prime factors of each array element and add them to a set to remove the duplicates
# and find the unique values only. Sieve of erastosthenos is used to find all primes up to n

import math
from typing import List
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        def prime_factors(n):
            
            # handle 2 and 3 separately
            for p in [2, 3]:
                while n % p == 0:
                    factors.add(p)
                    n //= p
            
            # only check 6k±1
            i = 5
            while i * i <= n:
                for candidate in [i, i+2]:   # 6k-1 and 6k+1
                    while n % candidate == 0:
                        factors.add(candidate)
                        n //= candidate
                i += 6
            
            if n > 1: #if after all division its left then do this
                factors.add(n)
            

        for num in nums:
            prime_factors(num)
        
        return len(factors)