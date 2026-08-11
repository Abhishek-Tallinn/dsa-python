# Problem: Leetcode 717 - 1-bit and 2-bit Characters
# Difficulty: Easy
# Link: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
# Time Complexity: O(n) as we iterate through the array once
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We iterate over the array with  a pointer and if we find a 2 bit character we jump index by 2 else by 1
# at the end of loop we check if the pointer is at last index or has gone beyond. because if its 
# on the last index then that means that last character was not part of a 2 bit character and was a one bit character.

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1:
                return True
        
        i = 0
        while i < len(bits)-1:
            if (bits[i]==1 and bits[i+1]==0) or (bits[i]==1 and bits[i+1]==1):
                i+=2
            else:
                i+=1
        return i == len(bits)-1