# Problem: Leetcode 2710 - Remove trailing zeros from a string
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/
# Time Complexity: O(k) where k are the number of trailing zeros
# Space Complexity: O(1)
# Approach: We iterate with a while loop to find the index of the last 0 on the right side and then we return the string slice till that index

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num)-1
        while i >= 0 and num[i]=='0':
            i-=1
        return num[:i+1]