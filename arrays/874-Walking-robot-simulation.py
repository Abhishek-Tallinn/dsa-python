# Problem: Leetcode 874 - Walking Robot Simulation
# Difficulty: Medium
# Link: https://leetcode.com/problems/walking-robot-simulation/description/
# Time Complexity: O(n + steps). n is the length of commands.
# Space Complexity: O(m) where m is length of obstacles
# Approach: Since obtacles look up is necessary we need to convert it to hashset for O(1) look up. 
# Then we need direction vector to switch direction to avoid boilerplate. Since direction vectors have value 0 or 1, we check if its possible to move one step before we actually take the step
# The direction is calculated using modulo operator as direction repeat after 4 movements.

from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x_pos = y_pos = 0
        max_dist = float('-inf')
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}
        d_vectors = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_index = 0
        for command in commands:
            if command == -2:
                dir_index = (dir_index-1)%4
            elif command == -1:
                dir_index = (dir_index+1)%4
            else:
                dx,dy = d_vectors[dir_index]
                for _ in range(command):
                    if (x_pos+dx,y_pos+dy) in obstacle_set:
                        break
                    x_pos+=dx
                    y_pos+=dy
                max_dist = max(max_dist, x_pos*x_pos+y_pos*y_pos) 
        return max_dist
   
