# Problem: Leetcode 1332 - Remove palindromic subsequences
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-palindromic-subsequences/description/
# Time Complexity: O(n) - as we reverse the string
# Space Complexity: O(n) as we reverse slice but we can do this with two pointers easily also
# Approach: The solution is in the realization that if a string is not already a palindrome which means it needs one operation,
# then the answer has to be two as it only has a and b and we can just take all a together and all b together and remove them in 2 operations
# as same character will always form a palindrome.

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]
        if is_palindrome(s):
            return 1
        return 2