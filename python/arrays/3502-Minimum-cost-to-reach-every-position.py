# Problem: Leetcode 3502 - Minimum cost to reach every position
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We keep a 'mn' and if current value is less we append current value else we keep appedning minimum 
# as per the conditions given in the problem as if the item at the higher index is bigger than we can 
# replace them with the mn value as replace with items behind is at no extra cost.

from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [cost[0]] 
        mn = cost[0]
        for i,cost in enumerate(cost[1:],1):
            if cost < mn:
                ans.append(cost)
                mn = cost
            else:
                ans.append(mn)
        return ans