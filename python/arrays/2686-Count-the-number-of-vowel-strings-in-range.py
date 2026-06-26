# Problem: Leetcode 2686 - Count the number of vowel strings in range
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We iterate over the words and for each word we check if first and last letter are vowels and index is inside the 
# range left to right. if yes then we increment our count

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        vowels = ('a','e','i','o','u')
        for idx,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels and idx>=left and idx<=right:
                cnt +=1
        return cnt
