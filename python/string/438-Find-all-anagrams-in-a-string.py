# Problem: Leetcode 438 - Find all anagrams in a string
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Time Complexity: O(n) - where n is the length of the input address
# Space Complexity: O(n) as we split the input array
# Approach1: We run a hashmap based sliding window where we keep a defaultdict with counter and keep incrementing each character count that we see
# and on each iteration we compare it to hashmap of p to check for anagram and if its true we increment our counter by 1. Also we check if index i is more than length of p
# meaning our substring will be longer than p and can never be an anagram we move our window forward to keep its length equal to length of p. 
# Since we use counter we can just decrement the value of the character on the leftmost part of window and beccause its a counter
# if the value of key goes to 0, it gets dropped automatically. if two hashmaps are equal we pick up the index of the first character in window 
# Appraoch2: we use a nested loop and take each substring of length equal to p change it to a counter and compare to P. It passes but is a slow solution

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = Counter(p)
        k = len(p)
        ans = []
        s_count = Counter()
        for i in range(len(s)):
            s_count[s[i]]+=1
            if i >= len(p):
                s_count[s[i-len(p)]]-=1
            if s_count==d:
                ans.append(i - len(p)+1)
            # old slower code but works
            #if Counter(s[i:i+k]) == d: #const comparison as 26 chars
            #    ans.append(i)
        return ans
        '''
        O(n*len(p)) solution TLE
        p = sorted(p)
        k = len(p)
        ans = []
        for i in range(len(s)):
            sub = s[i:i+k]
            if sorted(sub) == p:
                ans.append(i)
        return ans
        '''