# Problem: Leetcode 409 - Longest Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/Longest-Palindrom/description/
# Time Complexity: O(n) - passing over character of dictionary
# Space Complexity: O(n) as we have to produce the freq map
# Approach: We have to take all elements with even freq and for odd freq we take any odd freq element once with odd freq for the middle element. 
# For all other odd element we take 1 less character as we can use the even quantity

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        d = Counter(s)
        mx_length = 0
        odd_taken = False
        for char,freq in d.items():
            if freq%2==0:
                mx_length+=freq
            elif freq%2==1:
                if not odd_taken:
                    mx_length+=freq
                    odd_taken = True
                else:
                    mx_length+=(freq-1)
        return mx_length




        