# Problem: Leetcode 746 - Min Cost Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Time Complexity: O(n)
# Space Complexity: O(1) as we only keep last state
# Approach: Simple dp problem where in first appraoch we calculate the cost to leave the step i by adding the cost to leave step and min cost to arrive at that step
# approach2: we calculate as per the cost to reach step i but indexing is more complicated.

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
        '''
        dp = [0] * len(cost)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return min(dp[-1]+cost[-1],dp[-2]+cost[-2])
        '''