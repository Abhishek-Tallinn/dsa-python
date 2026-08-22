# Problem: Leetcode 3622 - Check divisibility by digit sum and product
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-divisbility-by-digit-sum-and-product/description/
# Time Complexity: O(k) as we need to sum the k digits
# Space Complexity: O(1)
# Approach: we calculate sum and product of digits and return true if their sum divides n

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = sum([int(d) for d in str(n)])
        p = 1
        for d in str(n):
            p *= int(d)
        return n%(s+p)==0