# Problem: Leetcode 2119 - A number after a double reversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/a-number-after-a-double-reversal/description/
# Time Complexity: O(n) as we loop rings once and then memo once
# Space Complexity: O(n) as we use memo hashmap
# Approach: Since reversed number can have leading zeros we convert it to a string once in the interim step
# before we return the value and then we compare original number string with the string of reversed reverse 


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse = int(str(num)[::-1])
        return str(num) == str(reverse)[::-1]
        