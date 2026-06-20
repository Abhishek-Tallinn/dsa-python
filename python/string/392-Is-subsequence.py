# Problem: Leetcode 392 - Is subsequence
# Difficulty: Easy
# Link: https://leetcode.com/problems/is-subsequence/description/
# Time Complexity: O(k) where k is the length of t
# Space Complexity: O(1)
# Approach: Since subsequence is not contiguous we just use two pointers. one pointer of T and other over s. when character of t is equal to character of s,
# then we increment the pointer of s. If the s pointer reaches the length of the string s then that means the it is a subsequence.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = j = 0
        while j<len(t) and i < len(s):
            if t[j] == s[i]:
                i+=1
            j+=1
        return i == len(s)