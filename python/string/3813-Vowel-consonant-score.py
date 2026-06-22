# Problem: Leetcode 3813 - Vowel consonant score
# Difficulty: Easy
# Link: https://leetcode.com/problems/vowel-consonant-score/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach2- we iterate over s and check each character. we keep count of vowels and consonants and at the end return v//c if c>0 else 0


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = c= 0
        vowels = {'a','e','i','o','u'}
        for char in s:
            if char in vowels:
                v+=1
            elif char.isalpha():
                c+=1
        return v//c if c>0 else 0