# Problem: Leetcode 3750 - Minimum number of flips to reverse binary string
# Difficulty: Easy
# Link: https://leetcode.com/problems/Minimum-number-of-flips-to-reverse-binary-string/description/
# Time Complexity: O(k) as we loop once where k is the number of bits
# Space Complexity: O(k) as we create the string with k bits
# Approach: We simply create the string s using bin function or we could also use a while loop. then the question is basically asking how many flips your need
# to make the string a palindrome. so you can loop once and compare the string value at index i to n-i-1 and the number of mismatches is what we need in our cnt variable.
# because we need that many flips


class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:] #automatically removes 0s
        #rev = s[::-1]
        cnt = 0
        for i in range(len(s)):
            if s[i]!=s[len(s)-i-1]:
                cnt+=1
        return cnt