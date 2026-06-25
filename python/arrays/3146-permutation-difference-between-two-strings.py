# Problem: Leetcode 3146 - Permutation difference between two strings
# Difficulty: Medium
# Link: https://leetcode.com/problems/permutation-difference-between-two-strings/description/
# Time Complexity: O(n +n +n) = O(n)
# Space Complexity: O(n) as we make two dictionaries
# Approach: we convert both string into hashmaps with value being index values. then we iterate over each char of s and see the absolute difference in the index values
# and add it to our answer


from collections import Counter
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d1 = {}
        d2= {}
        for idx,char in enumerate(s):
            d1[char] = idx
        for idx,char in enumerate(t):
            d2[char] = idx
        ans = 0
        for char in s:
            ans+=abs(d1[char]-d2[char])
        return ans