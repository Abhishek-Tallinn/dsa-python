# Problem: Leetcode 171 - Excel sheet column number
# Difficulty: Easy
# Link: https://leetcode.com/problems/excel-sheet-column-number/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Go from right to left and keep multiplying the ordinate value with a multiplier that keeps increasing by 26
# for each character from right to left 

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        mul=1
        for char in columnTitle[::-1]:
            num+=(ord(char)- 64)*mul
            mul*=26
    
        return num 