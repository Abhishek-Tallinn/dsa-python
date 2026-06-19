# Problem: Leetcode 266 - Palindrome Permutation
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-permutation/description/
# Time Complexity: O(n) as we iterate through string to make freq map
# Space Complexity: O(n) as use dictionary
# Approach: We simply count frequency of characters and we know that we are allowed to have only either 0 or 1 odd frequency character as 
# only one type of character is a palindrome ofcourse and if only one character has offcount the extra odd element can occupy the central place
# We cannot have odd freq more than 1


from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = Counter(s)
        odd_cnt = 0
        for value in d.values():
            if value%2==1:
                odd_cnt+=1
        return odd_cnt<=1