# Problem: Leetcode 2652 - Sum multiplies
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-multiplies/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Simple math problem. iterate and add elements which are divisible by either 3 or 5 or 7

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0
        for i in range(3,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                s+=i
        return s
