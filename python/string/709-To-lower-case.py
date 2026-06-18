# Problem: Leetcode 709 - To Lower Case
# Difficulty: Easy
# Link: https://leetcode.com/problems/t0-lower-case/description/
# Time Complexity: O(n) - convert each character to lowercase
# Space Complexity: O(1)
# Approach: we can use in built method or iterate over the string and convert each character to lower using ASCII
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        