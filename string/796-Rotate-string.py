# Problem: Leetcode 796 - Rotate String
# Difficulty: Easy
# Link: https://leetcode.com/problems/rotate-string/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: For simple solution we double the string and run a sliding window on it to match with goal. This has big O of O(n^2) and space of O(n) as for a for loop we have string slicing which is O(n).
# However, we can have another approach of substring search where we check in goal in s+s.
# This substring check directly uses in built KMP or Boyer Moore algorith which searches substring in O(n)
# we can further optimize the space complexity to O(1) by using two pointers and checking for each character in goal with the corresponding character in s with modulo operation. This will also have time complexity of O(n^2) though but saves space.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # O(n) solution
        return len(s)==len(goal) and goal in s+s
        #O(n^2) solution
        '''
        n = len(s)
        circular_s = s+s
        for right in range(1,n+1):
            if circular_s[right:right+n]==goal:
                return True
        return False
        '''
        