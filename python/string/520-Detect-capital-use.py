# Problem: Leetcode 520 - Detect Capital Use
# Difficulty: Easy
# Link: https://leetcode.com/problems/detect-capital-use/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: we simply check the conditions given in the question to to check isupper or islower or istitle. 


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(char.isupper() for char in word) or all(char.islower() for char in word):
            return True
        if word[0].isupper() and all(word[i].islower() for i in range(1,len(word))):
            return True
        return False