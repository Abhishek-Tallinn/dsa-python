# Problem: Leetcode 821 - Shortest Distance to a Character
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-distance-to-a-character/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we store the result
# Approach: Use two passes to calculate the shortest distance from each position to the nearest occurrence of the character.
# Two passes in opposite directions avoids the need to store all occurrences of the character and allows us to calculate the distance in a single pass each way.

from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float('inf')]*len(s)
        prev = float('inf')
        for i in range(len(s)):
            if s[i]==c:
                prev = i
            if prev!=float('inf'):
                ans[i] = i - prev
        prev = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                prev= i
            if prev!=float('inf'):
                ans[i] = min(ans[i], prev-i)
        return ans