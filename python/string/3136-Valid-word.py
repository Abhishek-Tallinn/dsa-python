# Problem: Leetcode 3121 - Valid word
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-word/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) as we only have a tuple of vowels
# Approach: We simply do simulation and check all the conditions while looping and return False is condition is not met. If loop ends then we return True

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        v = c = 0
        for char in word.lower():
            if char in ('a','e','i','o','u'):
                v+=1
            elif char.isalpha():
                c+=1
            elif (not char.isalpha()) and (not char.isdigit()):
                return False 
        if v == 0 or c==0:
            return False
        return True