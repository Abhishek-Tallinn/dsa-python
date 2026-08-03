# Problem: Leetcode 853 - Car Fleet
# Difficulty: Medium
# Link: https://leetcode.com/problems/car-fleet/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we have a stack 
# Approach: We sort the cars by position and then we simply iterate backwards and add the ending time of the cars in the stack. 
# If the time is less than stack[-1] means this fleet with join with last fleet as it will catch up but only when the time is greater than stack[-1] only then we add it to the stack.
# then we return length of the stack.

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(key=lambda x:x[0])
        stack = []
        for pos, spd in reversed(cars):  
            time = (target - pos) / spd
            
            if not stack or time > stack[-1]:
                stack.append(time)
            
    
        return len(stack)

        '''
        this logic not working as one car can catch multiple cars 
        and O(n^2) we cannot do as it will be TLE anyways
        for i in range(len(cars)-1):
            dist = cars[i+1][0] - cars[i][0]
            relative_speed = cars[i][1] - cars[i+1][1]
            print(relative_speed)
            if relative_speed <= 0:
                continue
            if cars[i+1][1]*(dist//relative_speed)) <= target - cars[i+1][0]:
                fleets-=1
        return fleets
        '''