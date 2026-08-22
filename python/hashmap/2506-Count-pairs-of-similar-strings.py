# Problem: Leetcode 2506 - Count pairs of similar strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-pairs-of-similar-strings/description/
# Time Complexity: O(n) as we loop over words
# Space Complexity: O(n) as we use a hashmap 
# Approach1: We make a hashmap and add each sorted word as key just like group anagrams. then for each key amount we know that the amount of pairs it can make
# can be known by the formula n*(n-1)//2.
# Approach2: we can use a nested loop to check every pairs as brute force is allowed

from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = {}
        for word in words:
            s = ''.join(set(sorted(list(word))))
            d[s] = d.get(s,0)+1
        pairs = 0
        for val in d.values():
            pairs += (val * (val-1))//2
        return pairs
        '''
        O(n^2) loop
        cnt = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if set(words[i]) == set(words[j]):
                    cnt+=1
        return cnt
        '''