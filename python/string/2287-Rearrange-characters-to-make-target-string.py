# Problem: Leetcode 2287 - Rearrange character to make target string
# Difficulty: Easy
# Link: https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use hashmaps
# Approach: we convert both to hashmaps and then the maximum time we can make target it the minimum availability of a character in our string s
# therefore for each character in t hashmap, we check by dividing how many possible time this character can be created from the total availability of this character in s
# and then we keep updating the minimum value as the minimum availability will decide how many targets can be made

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = Counter(s)
        t = Counter(target)
        mn = float('inf')
        for key,value in t.items():
            mn = min(mn,d[key]//value)
        return mn