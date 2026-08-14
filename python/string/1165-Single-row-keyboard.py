# Problem: Leetcode 1165 - Single row keyboard
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-row-keyboard/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(1). we may a hashmap but it has fixed sized
# Approach: We map each index in the hashmap and then we calculate how much jump we need from the prev character that we typed
# This we do by saving the index of current alphabet we typed into prev variable for calculating next jump.

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = {}
        for i,char in enumerate(keyboard):
            index[char] = i
        time = 0
        prev= 0
        for c in word:
            time+= abs(index[c]-prev)
            prev = index[c]
        return time
