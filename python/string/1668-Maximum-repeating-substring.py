# Problem: Leetcode 1668 - Maximum repeating substring
# Difficulty: Easy
# Link: https://leetcode.com/problems/max-repeating-substring/description/
# Time Complexity: O(n) as we perform join operations
# Space Complexity: O(n) as we make a string
# Approach: We simply keep increasing word by its own length and run a conditional while loop if word is 
# in the sequence and we keep incrementing our count variable and return cnt at the end.

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cnt = 0
        original = word
        while word in sequence:
            cnt+=1
            word+=original
        return cnt