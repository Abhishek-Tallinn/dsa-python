# Problem: Leetcode 504 - Base seven
# Difficulty: Easy
# Link: https://leetcode.com/problems/base-seven/description/
# Time Complexity: O(k) where k is the length of the answer string
# Space Complexity: O(k) as we store the string.
# Approach: We keep dividing the number by base 7 till it reaches 0 and at each level we keep taking the remainder for our 
# base 7 presentation. then we reverse the list and join it and return the answer. if number is negative
# which we have checked at the start with a flag, then we append a '-' sign on the front as well.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        baseSeven = []
        isNegative = num<0
        if isNegative:
            num = -num
        while num > 0:
            baseSeven.append(str(num%7))
            num = num//7
        if isNegative:
            baseSeven.append('-')
        return ''.join(baseSeven[::-1])