# Problem: Leetcode 3541 - Find most frequent vowel and consonant
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
# Time Complexity: O(n) as we go through the string
# Space Complexity: O(n) as we use the dictionary data structures
# Approach: We separate vowels and consonants from the string and made two freq hashmaps. Then we take max freq of each hashmap 
# or 0 if it does not exist and return the total

from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {'a','e','i','o','u'}
        vowels = []
        consonants = []
        for char in s:
            if char in v:
                vowels.append(char)
            else:
                consonants.append(char)
        vd = Counter(vowels)
        cd = Counter(consonants)
        f1 = f2 = 0
        if vd:
            f1 = max(vd.values())
        if cd:
            f2 = max(cd.values())
        return f1+f2