# Problem: Leetcode 1701 - Average Waiting Time
# Difficulty: Medium
# Link: https://leetcode.com/problems/average-waiting-time/description/
# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(1) as we only use a constant amount of extra space
# Approach: We simulate the process of serving customers in the original order and since 
# the first customer time is out of sync as they can arrive at any time we take their waiting time as their service time and also take initial finish time.
# For the rest of the customers we check if they arrive before the previous customer is done or after and calculate their waiting time accordingly.
# We keep a running total of the waiting time and return the average at the end.

from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_cust = len(customers)
        wait = customers[0][1]
        finish_time = (customers[0][0]+customers[0][1])
        for cust in customers[1:]:
            if cust[0] <= finish_time:
                finish_time+=cust[1]
            elif cust[0] > finish_time:
                finish_time = cust[0] + cust[1]
            wait += (finish_time - cust[0])
            
        return wait/total_cust