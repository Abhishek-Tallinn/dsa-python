# Problem: Leetcode 2144 - Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/
# Time Complexity: O(n log n) as we sort the cost array in reverse
# Space Complexity: O(1) as no extra data structure is used
# Approach: Sort the candies by cost and try to buy them in descending order, taking advantage of the discount for every third candy.
# Then return the total cost

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total = 0
        cnt = 0
        for c in reversed(cost):
            if cnt==2:
                cnt=0
                continue
            total+=c
            cnt+=1
        
        return total