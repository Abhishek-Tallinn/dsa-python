# Problem: Leetcode 748 - Shortest completing word
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-completing-word/description/
# Time Complexity: O(n) as we iterate through the array once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We add the freq of aphabets in a hashmap. then for each word we iterate over the hashmap and check if it has each key value >= the value of licensplate hashmap.
# If yes we return the word and to ensure it works we sort the words with key = len to ensure that shortest words come first


from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d = {}
        for char in licensePlate:
            if char.isalpha():
                d[char.lower()] = d.get(char.lower(),0)+1
        words.sort(key=len)
        for word in words:
            temp = Counter(word)
            found = True
            for key,val in d.items(): 
                if val > temp[key]:
                    found = False
                    break
            if found:
                return word
                