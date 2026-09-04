# Problem: Leetcode 1657 - Determine if two strings are close
# Difficulty: Medium
# Link: https://leetcode.com/problems/determine-if-two-strings-are-close/description/
# Time Complexity: O(n) as we loop hashmaps separately
# Space Complexity: O(n+n) as we makes hashmaps
# Approach: We check first that both strings should have same characters by converting to a hashmap
# if they pass this test then we convert their frequencies into a hashmap and check that both these hashmaps are equal
# because frequencies can be interchanged by the operation but the number of each frequency cannot be amended or a freq cannot be added or removed
# they only shuffle. So hashmap of the frequencies itself should be equal to check if strings are actually equal.


from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1==word2:
            return True
        if len(word1)!=len(word2):
            return False
        w1 = Counter(word1)
        w2 = Counter(word2)
        v1 = Counter(w1.values())
        v2 = Counter(w2.values())
        for ch,val in w1.items():
            if ch not in w2 or val not in v2:
                return False
        for ch,val in w2.items():
            if ch not in w1 or val not in v1:
                return False
        return v1==v2