# Problem: Leetcode 2716 - Minimize string length
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimize-string-length/description/
# Time Complexity: O(1)
# Space Complexity: O(n)
# Approach: The code is based on realization that its just asking for the number of unique characters in the string as you can remove all repetitions but not one occurrence of the character.



class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
