# Problem: Leetcode 2126 - Destroying Asteroids
# Difficulty: Medium
# Link: https://leetcode.com/problems/destroying-asteroids/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: Sort the asteroids by size and try to destroy them in ascending order, starting with the given mass.
# If at any point the mass is less than the size of the asteroid, we cannot destroy it and return False. If we successfully destroy all asteroids, we return True. 

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        total = mass
        for asteroid in asteroids:
            if total < asteroid:
                return False
            total += asteroid

        return True