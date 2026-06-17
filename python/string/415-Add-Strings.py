# Problem: Leetcode 415 - Add strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-strings/description/
# Time Complexity: O(n+k) - passing over each character of two number strings so O(n)+O(n) is O(n) and then while look for k digits
# Space Complexity: O(k) which is length of answer string with k digits
# Approach: This is a a problem which teaches on converting strings to integer and int to str without using inbuilt function to convert the whole things at once.
# so i am converting str to an integer digit and then back using  ASCII table values.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1=0
        for digit in num1:
            n1 = n1*10+(ord(digit)-ord('0'))
        n2=0
        for digit in num2:
            n2 = n2*10 + (ord(digit)-ord('0'))
        total = n1+n2
        
        ans = ""
        while total>0:
            digit = total%10
            ans = chr(digit+ord('0')) + ans
            total = total//10
        return ans if ans else "0"