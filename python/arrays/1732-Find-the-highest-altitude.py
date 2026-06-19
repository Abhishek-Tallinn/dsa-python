# Problem: Leetcode 1732 - Find the highest altitude
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-highest-altitude/description/
# Time Complexity: O(n) as we move through gain array
# Space Complexity: O(1)
# Approach: We simply keep updating the height at current index and keep a mx variable which keep track of max value and we return mx


from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hi = 0
        mx = 0
        for g in gain:
            hi = hi+g
            mx = max(mx,hi)
        return mx