# Problem: Leetcode 3516 - Find closest person
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-closest-person/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Since speed is same just return based on the absolute distance between person 1 and 3 and person2 and 3

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        time_x = abs(x-z)
        time_y = abs(y-z)
        if time_x < time_y:
            return 1
        elif time_x > time_y:
            return 2
        return 0