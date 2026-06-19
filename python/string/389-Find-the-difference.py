# Problem: Leetcode 389 - Find the difference
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-difference/description/
# Time Complexity: O(n) - as we create hashmaps
# Space Complexity: O(k) where k is the length of strings
# Approach: We convert both string to hashmaps as frequencies are important here. then for character in t we check that 
# if char not in hashmap of s or if it is then its freq is not the same then we return the char 


from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = Counter(s)
        t_map = Counter(t)
        for char,freq in t_map.items():
            if char not in s_map or freq != s_map[char]:
                return char 