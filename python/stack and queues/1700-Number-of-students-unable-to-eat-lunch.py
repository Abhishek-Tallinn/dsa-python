# Problem: Leetcode 1700 - Number of students unable to eat lunch
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
# Time Complexity: O(n) as we loop over s
# Space Complexity: O(n+m) as we have to use deques
# Approach: We convert both to a deque and then we loop till student queue is not empty. But his can lead to infinite loop
# so we then ensure that we keep an unable counter which increments everytime a student is not able to take a top sandwich
# and if this counter reach the current length of s then that means that top sandwich cannot be picked up
# and we break the loop


from collections import deque
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(students)
        sand = deque(sandwiches)
        unable =0
        while s:
            if s[0] == sand[0]:
                s.popleft()
                sand.popleft()
                unable = 0
            else:
                s.append(s.popleft())
                unable+=1
                if unable == len(s):
                    break
        return len(s)
        #counting appraoch is also possible where we coutn how many want
        # circle and how many want square. then we iterate over
        # sandwiches and we see if top sandwich can be picked up or no by comparing the counts.
        #  if yes then we decrement the relevant sandwich else we directly return 
        # the remaining students count.
