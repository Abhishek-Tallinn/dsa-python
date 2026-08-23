# Problem: Leetcode 4030 - Check ASCII palindromic
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-ASCII-palindromic/description/
# Time Complexity: O(n)
# Space Complexity: O(n) to store ans to check for palindromic
# Approach - We take each character in the string and convert its ascii value to a binary value and then concatenate that string together to get our final string.
# since lowercase character values are between 97 to 122 they will all have 7 bits so we pad them with with one 0. 
# Then we return the check if ans is equal to its reverse

class Solution:
    def isPalindromic(self, s: str) -> bool:
        ans = []
        for char in s:
            val = '0'+bin(ord(char))[2:]

            ans.append(val)
        ans = ''.join(ans)
        
        return ans==ans[::-1]