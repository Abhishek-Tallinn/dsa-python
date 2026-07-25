# Problem: Leetcode 3536 - Maximum product of two digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/Maximum-product-of-two-digits/description/
# Time Complexity: O(1) as only ten digits
# Space Complexity: O(1) as only 10 digits
# Approach: we simply extract and sort the digits and multiply the biggest 2 and return

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort()
        return digits[-1]*digits[-2]