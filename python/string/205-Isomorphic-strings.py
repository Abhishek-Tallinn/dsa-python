# Problem: Leetcode 205 - Isomorphic Strings
# Difficulty: East
# Link: https://leetcode.com/problems/isomorphic-strings/description/
# Time Complexity: O(n) as we iterate through one string
# Space Complexity: O(n) as we make hashmap in our main approach.
# Approach: We make two hashmap and maintain a map of unique characters. We then see that if a key is found
# in first hashmap then we check if its mapped to the same character as earlier in the second hashmap
# and we also check the opposite way that if character of t is found in second hashmap and its not mapped for same 
# character in first hashmap then we directly return False.
# Approach2: we can directly club the elements by zipping them and making a set to remove duplicates
# then length of this set should be equal to the len(set(first string)) an len(Set(secondstring)) because
# if zip produces the same pairs which are repeated and then will be removed in the set and then length of sets
# will come out to be same

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
        '''
        return list(map(s.index,s)) == list(map(t.index,t))
        '''

        '''
        d_s = {}
        d_t = {}
        for i in range(len(s)):
            if (s[i] in d_s and d_s[s[i]] != t[i]) or (t[i] in d_t and d_t[t[i]]!=s[i]):
                return False
            d_s[s[i]] = t[i]
            d_t[t[i]] = s[i]
        return True
        '''