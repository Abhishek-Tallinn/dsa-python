# Problem: Leetcode 3456 - Find special substring of length k
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-special-substring-of-length-k/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We loop through characters of the string and we add to count variable. If a diff character is found and count is k then we immediately return true.
# but on finding different character is count is not k then we reset count to current character so we reset it to 1

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = 1 #chars own count
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else: #will fire only when character not equal
                if count==k:
                    return True
                count=1
        return count==k