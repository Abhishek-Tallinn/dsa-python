# Problem: Leetcode 735 - Asteroid Collision
# Difficulty: Medium
# Link: https://leetcode.com/problems/asteroid-collision/description/
# Time Complexity: O(n) as we iterate through the list
# Space Complexity: O(n) 
# Approach1: We append positive asteroid straight. for negative we pop till asteroid is stronger than stack[-1] and also stack[-1] is a right moving asteroid
# once popping is done if stack is empty or stack[-1] is a left moving asteroid we append the negative asteroid.
# if this is not so and the stack exists and stack[-1] is exactly equal to our left moving asteroid we just pop and stack one and done append.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1]>0 and abs(asteroid)> stack[-1]:
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(asteroid)
                    continue
                if abs(asteroid)==stack[-1]:
                    stack.pop() #pop once and dont append
                
            else:
                stack.append(asteroid)
            
        return stack