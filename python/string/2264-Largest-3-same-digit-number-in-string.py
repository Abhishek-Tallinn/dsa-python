# Problem: Leetcode 2264 - Largest 3 same digit number in string
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
# Time Complexity: O(n) 
# Space Complexity: O(1) 
# Approach: We simply do index based check if 3 digits are same if yes then we slice it and compare with mx and 
# update our mx variable accordingly.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                sub = num[i:i+3]
                mx = max(mx,sub)
        return mx