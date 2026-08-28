# Problem: Leetcode 2952 - Minimum number of coins to be added
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) as we only use pointers
# Approach: We take max_reachable which is 1 higher than the actual value which is reachable. If the current coin value is less than or equal to max_reachable, then
# the max_reachable increases by next amount and we have to add that coin. If current coin value is greater than max_reachable then 
# it means there are some values in the GAP which cannot be reached so we have to add a coin equal to value of max_reachable which means
# than max_reachable now double and we increase our coin count by 1.

from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        max_reachable = 1
        coin_index = 0
        cnt = 0
        while max_reachable<=target:
            if coin_index<len(coins) and coins[coin_index] <= max_reachable:
                max_reachable += coins[coin_index]
                coin_index+=1
            else:
                max_reachable<<=1
                cnt+=1
        return cnt