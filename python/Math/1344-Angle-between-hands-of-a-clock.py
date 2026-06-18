# Problem: Leetcode 1344 - Angle between hands of a clock
# Difficulty: Medium
# Link: https://leetcode.com/problems/ange-between-hands-of-a-clock/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: Its a simple math problem. By given minutes input we can calculate the minutes angle directly. Then based on minutes we 
# calculate how much the hour hand has travelled and then calculate the hour angle based on its total travel. 
# Then we just calculate the difference between them and return the the min of diff or 360 - diff

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_travel = float((minutes)*(5/60))
        minutes_angle = float((minutes)* (360/60))
        hour_angle = hour*30 + hour_travel * 6
        return min(abs(hour_angle-minutes_angle),360-abs(hour_angle-minutes_angle))