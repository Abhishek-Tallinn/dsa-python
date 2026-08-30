# Problem: Leetcode 2299 - Strong password checker II
# Difficulty: Easy
# Link: https://leetcode.com/problems/strong-password-checker-II/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use hashmaps
# Approach: we simply perform the checks as provided in the question and return False if any of the conditions fail.
# other wise we return true

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                return False
        upper = lower = digit = special = 0
        for char in password:
            if char.isupper():
                upper+=1
            elif char.isdigit():
                digit+=1
            elif not char.isalnum():
                special+=1
            else:
                lower+=1
        if lower<1 or upper<1 or digit<1 or special<1:
            return False
        return True