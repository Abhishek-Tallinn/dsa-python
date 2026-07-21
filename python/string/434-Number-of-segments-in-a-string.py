# Problem: Leetcode 434 - Number of segments in a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-segments-in-a-string/description/
# Time Complexity: O(n) - where n is the length of the input address
# Space Complexity: O(n) as we split the input array
# Approach: just strip any spaces and then count length on splitting which will ignore the middle spaces itself.

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        return len(s.split())