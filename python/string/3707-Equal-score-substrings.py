# Problem: Leetcode 3707 - Equal score substrings
# Difficulty: Easy
# Link: https://leetcode.com/problems/equal-score-substrings/description/
# Time Complexity: O(n) as we loop through the string 
# Space Complexity: O(1) as we only use the length pointer
# Approach: We iterate once to find the total score. If score is off we cannot split into two equal halves.
# if score is even we iterate again maintaining current sum and if at any points its equal to total//2 we return True.
# if loop ends we return False


class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = 0
        for char in s:
            total+=(ord(char)-ord('a') + 1)
        if total%2==1:
            return False
        curr_sum = 0
        for char in s:
            curr_sum+=(ord(char)-ord('a')+1)
            if curr_sum == total//2:
                return True
        return False