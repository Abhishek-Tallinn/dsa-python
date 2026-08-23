# Problem: Leetcode 2515 - Shortest distance to target string in circular array
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-distance-to-target-string-circular-array/description/
# Time Complexity: O(n) as we do two loops
# Space Complexity: O(1) as we only use two pointers
# Approach: We iterate on both sides and capture distance and update our mn variable to see which side the minimum distance occurs on.
# in both iteration on both sides we do basically len(words) iteration but to rotate the index we do i%n and i+n%n so that all values get covered
# to track the distance we can keep a distance variable and use it in to updat the mn distance 
# or we can just do it directly with startIndex and i

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
      mn = float('inf')
      n = len(words)
      for i in range(startIndex, startIndex + len(words)):
          if words[(i)%n] == target:
              mn = min(mn, abs(startIndex-i))
      dist=0
      for i in range(startIndex+n, startIndex,-1):
          if words[(i+n)%n] == target:
              mn = min(mn, abs(startIndex-(i-n)))
      if mn!= float('inf'):
          return mn
      return -1