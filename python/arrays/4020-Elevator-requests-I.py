# Problem: Leetcode 4020 - Elevator requests I
# Difficulty: Easy
# Link: https://leetcode.com/problems/Elevator-requests-I/description
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We iterate on array and calculate time to move to each floor from prev floor

from typing import List

class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        prev_floor = 0
        for r in requests:
            total_time+=abs(r-prev_floor)
            prev_floor = r
        return total_time