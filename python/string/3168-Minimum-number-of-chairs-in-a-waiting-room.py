# Problem: Leetcode 3168 - Minimum number of chairs in a waiting room
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We go through even and see how mnay chairs we need at any time. then we update the mx variable
# which keeps track of the max chairs required at any time

class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        mx = 0
        for event in s:
            if event=="E":
                chairs+=1
            elif event=="L":
                chairs-=1
            mx = max(mx,chairs)
        return mx