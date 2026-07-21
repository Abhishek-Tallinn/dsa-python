# Problem: Leetcode 521 - Longest uncommon subsequence I
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-uncommon-subsequence/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: If both string are not exactly equal then subsequence which is not common will just be the longer string
# and it they are absolutely equal then we return -1


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a!=b:
            return max(len(a),len(b))
        return -1