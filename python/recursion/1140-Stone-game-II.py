# Problem: Leetcode 1140 - Stone game II
# Difficulty: Medium
# Link: https://leetcode.com/problems/stone-game-ii/description/
# Time Complexity: O(n^2) where n is the length of the array
# Space Complexity: O(n^2) for the memoization table
# Approach1: We use the minimax algorithm with memoization where each player tries to maximize their score and minize the opponent's score
# We use a prefix sum array to calculate the sum of stones in O(1) time. The dp function takes the starting index and the maximum number of piles that can be taken and returns the maximum number of stones that can be obtained by the current player.
# the main trick is that prefix array return the available stones  for that particular valid move and we subtrack the recursive value 
# for next iteration which will be picked by other player thereby maximizing the stones that the player can take.

from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dp(start_index,max_take):
            if max_take*2 >= total_piles - start_index:
                return prefix[total_piles] - prefix[start_index]
            mx_stones = 0
            for num_piles_to_take in range(1, 2 * max_take + 1):
                stones_obtained = prefix[total_piles] - prefix[start_index] - \
                                 dp(start_index + num_piles_to_take, 
                                   max(max_take, num_piles_to_take))
                mx_stones = max(mx_stones, stones_obtained)
            return mx_stones

        
        total_piles = len(piles)
        prefix = [0]
        for pile in piles:
            prefix.append(pile+prefix[-1])


        return dp(0,1)