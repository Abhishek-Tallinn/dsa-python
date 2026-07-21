# Problem: Leetcode 557 - Reverse words in a String III
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Time Complexity: O(n) - passing over each character of string and reversing and splitting
# Space Complexity: O(n) as we make a list and join it back
# Approach: We split the string and then reverse each word separately and join each element of the resulting list with a space in between.

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans = [word[::-1] for word in l]
        return ' '.join(ans)