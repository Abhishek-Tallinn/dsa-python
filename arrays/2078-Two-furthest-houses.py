# Problem: Leetcode 2078 - Two Furthest Houses With Different Colors
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: To find the two furthest houses with different colors, we can iterate through the list and keep track of the indices of the first and last houses with each color. Then, we calculate the maximum distance between these indices.
# The intuition is to realise that furthest distance will include either the first or the last house. So we can check the distance between the first house and the last house of a different color, and the distance between the last house and the first house of a different color.

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        if n==2:
            return 1
        max_distance = 0
        for i in range(len(colors)):
            if colors[0]!=colors[n-1-i] or colors[n-1]!=colors[i]:
                return n-i-1