# Problem: Leetcode 3407 - Substring pattern matching
# Difficulty: Easy
# Link: https://leetcode.com/problems/substring-pattern-matching/description/
# Time Complexity: O(n+n) as make make parts array with for loop and we do find and rfind
# Space Complexity: O(n) as we make parts 
# Approach: To match wildcard we simply split the string at '*' and remove empty string. then if after splitting there is only one part meaning that the * was first or last element
# then we check if remaining string was in s and return T/F. But if * was not on edge, then we first find the first part of the string using find in built function,
# and then we find the second part after the * using find but the starting index is after the first part ends which means its searching in the remaining part of the string for second part.
# if second part is found in string after the ending index of first part we just return true. else we return false


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        for char in p:
            if char!='*' and char not in s:
                return False
        parts = [x for x in p.split('*') if x!='']
        if not parts:
            return True
        if len(parts)==1:
            return parts[0] in s
        left = s.find(parts[0])
        if left == -1:
            return False
        right = s.find(parts[1], left + len(parts[0]))

        return right != -1