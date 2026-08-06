# Problem: Leetcode 3345- Smallest divisible digit product I
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Its a simple math problem. We can run loop from n to sys.maxsize and for each number we can calculate the product of its digits and check if it is divisible by t. If yes we return that number.

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        mx=10**20
        for i in range(n,mx):
            prod = 1
            for digit in str(i):
                prod*=int(digit)
            if prod%t==0:
                return i