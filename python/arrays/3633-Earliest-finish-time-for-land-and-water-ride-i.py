# Problem: Leetcode 3633 - Earliest Finish Time for Land and Water Ride I
# Difficulty: Easy
# Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-ride-i/description/
# Time Complexity: O(nlogn + mlogm) where n and m are the lengths of the respective arrays
# Space Complexity: O(n+m) as i zip the arrays together and sort them.
# Approach: We calculate the earliest finish times for both by calculating the sequence for land-water and then for water-land and then returning the minimum of the two. 
# In the second appraoch which does not use a helper function but try to zip the start and end time together and then calculate the total earliest time.
# In this problem the constraints are small so we can also do an O(n^2) appraoch which will also work.

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
        '''
        landEndTime=[]
        for i in range(len(landStartTime)):
            landEndTime.append(landStartTime[i]+landDuration[i])
        waterEndTime=[]
        for j in range(len(waterStartTime)):
            waterEndTime.append(waterStartTime[j]+waterDuration[j])
        land = list(zip(landStartTime,landEndTime))
        water = list(zip(waterStartTime,waterEndTime))
        land.sort(key = lambda x:x[1])
        water.sort(key = lambda x:x[1])
        land_water = float('inf')
        water_land = float('inf')
        for i in range(len(water)):
            land_water = min(land_water,max(land[0][1],waterStartTime[i]) + waterDuration[i]) #because the duration is not zipped together
        for i in range(len(land)):
            water_land = min(water_land , max(water[0][1], landStartTime[i]) + landDuration[i])
        return min(land_water,water_land)
        # in such questions try to zip everything so they move together
        '''
        

        
            

        
            
        
        
        