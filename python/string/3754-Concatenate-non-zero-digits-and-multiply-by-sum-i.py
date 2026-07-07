# Problem: Leetcode 3754 - Concatenate Non-Zero Digits and Multiply by Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum/description/
# Time Complexity: O(k) as we loop once where k is the number of digits
# Space Complexity: O(k) as we create the string with k digits
# Approach: We iterate through each digit of the number, concatenate non-zero digits, and calculate the sum of non-zero digits. Then we multiply the concatenated number by the sum.
# if in case the there are no non-zero digits then we just return 0.
# 

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = []
        total = 0
        for d in str(n):
            if d!='0':
                ans.append(d)
                total+=int(d)
        if not ans:
            return 0
        new_n = int(''.join(ans))
        return new_n * total