# Problem: Leetcode 2259 - Remove digit from number to maximize result
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We compare string lexicographically after removing the digit each time we find it and take the max result

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        mx = ""
        for i in range(len(number)):
            if number[i] == digit:
                mx = max(mx, number[:i]+number[i+1:])
        return mx