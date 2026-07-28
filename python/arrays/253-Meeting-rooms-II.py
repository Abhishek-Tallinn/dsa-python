# Problem: Leetcode 253 - Meeting rooms II
# Difficulty: Medium
# Link: https://leetcode.com/problems/meeting-rooms-ii/description/
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Approach: We simply sort the intervals anc check for overlap from each meetings ending time to start of next meeting.
# we keep a boolean array of True as each meeting needs a room. But during our nested loop if a meeting can release a room for a future meeting
# then we mark the future meetings as False as it would not need its own room. We keep marking future meetings as false for each meeting in the loop
# Only one thing we need to keep in mind that in case we can mark a meeting as False but its already False as an earlier meeting marked it as False
# then we continue forward. Also after marking one meeting as false we break the inner loop as one meeting can release the room only for one future meeting.
# any further future concerns are of the future meetings.

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        rooms = [True]*len(intervals)
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if intervals[i][1]<=intervals[j][0]:
                    if not rooms[j]:
                        continue
                    rooms[j] = False
                    break
        cnt = 0
        for room in rooms:
            if room:
                cnt+=1
        return cnt
