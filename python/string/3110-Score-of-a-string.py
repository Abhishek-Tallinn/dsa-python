# Problem: Leetcode 3081 - Score of a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/score-of-a-string/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We iterate through the string and take the difference of each pair ASCII values

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1,len(s)):
            score += abs(ord(s[i])-ord(s[i-1]))
        return score