# Problem: Leetcode 2904 - Shortest and lexicographically smallest beautiful string
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
# Time Complexity: O(n)
# Space Complexity: O(n) 
# Approach: we maintain a valid sliding window where the number of 1s in window are equal to k. If 1s in current window are equal to k
# then we take the substring and compare it to our candidate and update the candidate.

from collections import defaultdict
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # hashmap based sliding window
        if s.count('1') < k:
            return ""
        candidate = '1'*len(s)
        ones = 0
        left = 0
        d={}
        for right in range(len(s)):
            if s[right]=='1':
                ones+=1
            d[right]=ones
            while left<right and (d[right]-d[left]+ (1 if d[left]>0 else 0) > k or s[left]=='0'):
                left+=1
            if d[right] - d[left] + (1 if d[left]>0 else 0)== k:
                sub = s[left:right+1]
                if len(sub) < len(candidate):
                    candidate = sub
                elif len(sub) == len(candidate) and sub < candidate:
                    candidate = sub
        return candidate
        '''
        if s.count('1')<k:
            return ""
        prefix = [0]*(len(s)+1)
        ones = 0
        for i in range(len(s)):
            if s[i]=='1':
                ones+=1
            prefix[i+1] = ones
        left = 0
        candidate = '1'*len(s)
        for right in range(len(s)):
            while left < right and (prefix[right+1] - prefix[left] > k or s[left]=='0'):
                left+=1
            if prefix[right+1] - prefix[left] == k:
                sub = s[left:right+1]
                if len(sub) < len(candidate):
                    candidate = sub
                elif len(sub) == len(candidate) and sub<candidate:
                    candidate = sub
        return candidate
        '''
        '''
        #brute force works
        candidate = '1'*len(s)
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if sub.count('1')==k:
                    if len(sub) < len(candidate):
                        candidate = sub
                    elif len(sub) == len(candidate):
                        if sub<candidate:
                            candidate = sub
        return candidate
        '''
