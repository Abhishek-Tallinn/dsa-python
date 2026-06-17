# Problem: Leetcode 412 - Fizz Buzz
# Difficulty: Easy
# Link: https://leetcode.com/problems/fizz-buzz/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(n) as we have to produce the results array
# Approach: This is a simple simulation problem where we loop from 1 to n and populate the result array as per conditions

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res= []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%5==0:
                res.append("Buzz")
            elif i%3==0:
                res.append("Fizz")
            else:
                res.append(str(i))
        return res