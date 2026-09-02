# Problem: Leetcode 1704 - Determine if Strings Halves Are Alike
# Difficulty: Easy
# Link: https://leetcode.com/problems/determine-if-strings-halves-are-alike/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We split the string and compare the cnt of vowels in the two halves to return true or false

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        first = s[:n//2]
        second = s[n//2:]
        vowels = ('a','e','i','o','u')
        return sum(1 for char in first if char.lower() in vowels) == sum(1 for char in second if char.lower() in vowels)