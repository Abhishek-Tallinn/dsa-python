# Problem: Leetcode 2446 - Determine if two events have conflict
# Difficulty: Easy
# Link: https://leetcode.com/problems/determine-if-two-events-have-conflict/description/
# Time Complexity: O(1)
# Space Complexity: O(1) as no extra data structure is used
# Approach1: We check both sides that if the starting time of event2 is earlier than event1 then we switch them.
# Then we take the hour and minutes of event1 end time and hour and minutes of event2 start time and check their integer values to determine what comes earlier.
# Approach2: We dont need integer comparison as lexicographical comparison can make our task mush easier.
# Since event2 can start before event1 we just check both ways if event1 end time is less than event2 start time or event2 end time is less than event1 start time.
# and since we have to return true in conflict we return 'not' so that true is returned if there is conflict

from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        return not (event1[1]<event2[0] or event2[1] < event1[0])
        '''
        if event2[0].split(":")[0] < event1[0].split(":")[0]:
            event1,event2=event2,event1
        if event2[0].split(":")[0] == event1[0].split(":")[0]:
            if event2[0].split(":")[1] < event1[0].split(":")[1]:
                event1,event2 = event2,event1
        event1endhour,event1endmin = event1[1].split(":")
        event2starthour,event2startmin = event2[0].split(":")
        if int(event1endhour) > int(event2starthour):
            return True
        if int(event1endhour) == int(event2starthour):
            if int(event1endmin) >= int(event2startmin):
                return True
        return False 
        '''