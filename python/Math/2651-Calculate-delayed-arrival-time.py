# Problem: Leetcode 2651 - Calculate delayed arrival time
# Difficulty: Easy
# Link: https://leetcode.com/problems/calculate-delayed-arrival-time/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Simple math problem. if time is 24 return 0 else time%24

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        final = arrivalTime+delayedTime
        return 0 if final==24 else final%24