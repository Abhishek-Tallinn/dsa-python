# Problem: Leetcode 3019 - Number of changing keys
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-changing-keys/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: since bigger and smaller keys are same we first convert string to lower string. then we 
# just count the number of changes in string where character is not equal to preceding character.


class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0
        s = s.lower()
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                cnt+=1
        return cnt