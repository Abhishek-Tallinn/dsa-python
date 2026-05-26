# Problem: Leetcode 3120 - Count the Number of Special Characters I
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
# Time Complexity: O(n) as we loop through the set made from string
# Space Complexity: O(n) as we use a set which can be of length n
# Approach: Simple approach that since we have to check 'membership' we loop through the set and we check if a character is lowercase then does 
# its uppercase version is also in the set. Checking in string or list would make this O(n2) but in a set its O(n) overall.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        cnt = 0

        for char in word:
            if char.islower() and char.upper() in word:
                cnt+=1

        return cnt
        