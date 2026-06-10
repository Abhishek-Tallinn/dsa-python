# Problem: Leetcode 455 - Assign Cookies
# Difficulty: Easy
# Link: https://leetcode.com/problems/assign-cookies/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)
# Approach: Sort both arrays and use a greedy approach to assign the smallest available cookie to each child. 
# If we are able to satisfy a child with current cookie then we move to the next child

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        i = 0
        for j in range(len(s)):
            if s[j]>=g[i]:
                cnt+=1
                i+=1
                if i == len(g):
                    break
        return cnt
        '''
        while i < len(g) and j < len(s):
            if s[j]>=g[i]:
                cnt+=1
                i+=1
            j+=1
        return cnt
        '''