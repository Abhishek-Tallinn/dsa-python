# Problem: Leetcode 1854 - Maximum population year
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-population-year/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1) as array is 101 constant size
# Approach: Since years are from 1950-2050 we keep an array of 101 length and iterate over logs and keep increment count of 
# each year that comes as we are basically marking many people are alive in each year and we always offset index 
# by 1950 as 1950 corresponds to 0 index. then we also keep track of mx_pop and then we return the target year index + 1950 
# to get correct answer.

from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort(key=lambda x:x[0])
        total_pop = [0]*101
        mx_pop = 0
        for i in range(len(logs)):
            for j in range(logs[i][0],logs[i][1]):
                total_pop[j-1950]+=1
                mx_pop = max(mx_pop,total_pop[j-1950])

        for i,pop in enumerate(total_pop):
            if pop == mx_pop:
                return i + 1950