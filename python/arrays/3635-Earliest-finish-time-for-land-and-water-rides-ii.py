# Problem: Leetcode 3633 - Earliest Finish Time for Land and Water Ride II
# Difficulty: Medium
# Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-ride-ii/description/
# Time Complexity: O(n + m) where n and m are the lengths of the respective arrays as we dont sort here
# Space Complexity: O(n+m) as i zip the arrays together and sort them.
# Approach: We calculate the earliest finish times for both by calculating the sequence for land-water and then for water-land and then returning the minimum of the two. 
# In the second appraoch which does not use a helper function but try to zip the start and end time together and then calculate the total earliest time.
# Due to higher constrains this question does not allow an O(n^2) appraoch as it will cause TLE.


from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve(start1, duration1, start2, duration2):
            finish1 = float('inf')
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])
            finish2 = float('inf')
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1)+duration2[i])
            return finish2
        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve(waterStartTime,waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)