# Problem: Leetcode 3461 - Check if digits are equal in string after operations i
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/
# Time Complexity: O(n^2) since we use nested loops
# Space Complexity: O(n) as we generate new string which is at least n-1 length at each step
# Approach: We simply use a while loop for looping till length of s becomes 2 which is our requirement.
# in every loop we make a temp list and with a for loop club the digits and add to temp. after the for loop we 
# reassign the list as a string to s and then work again with the new string.



class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2: #use explicit condition instead of true
            temp = []
            for i in range(len(s)-1):
                val = (int(s[i]) + int(s[i+1]))%10
                temp.append(str(val))
            s = ''.join(temp)
        return s[0]==s[1]
