# Problem: Leetcode 3794 - Reverse String prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-string-prefix/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make two slices which equal total string length
# Approach: We simply slice the part which we have to reverse and slice the remaining part also and 
# we just return the their sum which is our target string

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        first_k = s[:k][::-1]
        rem = s[k:]
        return first_k+rem