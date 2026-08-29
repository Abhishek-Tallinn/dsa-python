# Problem: Leetcode 2273 - Find resultant array after removing anagrams
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/
# Time Complexity: O(n) as out check anagram function uses a count array
# Space Complexity: O(1) as no extra data structure is used
# Approach: We check each pairs of words and have length check to not test useless words and then we 
# if they are anagram we just continue and if not then we insert the new current element into the array.

from collections import Counter
from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def check_anagram(s,t):
            count = [0]*26
            for c1,c2 in zip(s,t):
                count[ord(c1)-ord('a')]+=1
                count[ord(c2)-ord('a')]-=1
            return all(c==0 for c in count)

        ans = [words[0]]
        for i in range(1,len(words)):
            if len(words[i]) == len(words[i-1]):
                if check_anagram(words[i],words[i-1]):
                    continue
            ans.append(words[i])
               
        return ans