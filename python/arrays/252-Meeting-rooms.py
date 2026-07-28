# Problem: Leetcode 252 - Meeting rooms
# Difficulty: Easy
# Link: https://leetcode.com/problems/meeting-rooms/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: We simply sort the intervals and check for overlap in a loop and return False if overlap is found
# otherwise we return true

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True