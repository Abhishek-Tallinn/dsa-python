# Problem: Leetcode 3498 - Reverse degree of a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-degree-of-a-string/description/
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) as we just check in the array
# Approach: We iterate throught the string and calculate the reversed index of each character and multiply it with its current index in s 
# and maintain a total which we return at the end

class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for idx,char in enumerate(s):
            idx_rev = 26- (ord(char)-ord('a'))
            total += (idx_rev*(idx+1))
        return total