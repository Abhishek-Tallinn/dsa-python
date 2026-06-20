# Problem: Leetcode 383 - Ransom Note
# Difficulty: Easy
# Link: https://leetcode.com/problems/ransom-note/description/
# Time Complexity: O(len(ransomNote)) - passing over hashmap of ransomNote
# Space Complexity: O(n+n) - as we create two hashmaps
# Approach: to find character frequencies we convert both to hashmaps. then we iterate over the ransomNote hashmap as this is the one we need to create
# if a character in ransomNote is not in hashmap of magazine or the freq of a character is greater than how many are available in magazine we return False. If loop ends we return true.


from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(ransomNote)
        d1 = Counter(magazine)
        for char,freq in d.items():
            if char not in d1 or freq > d1[char]:
                return False
        return True