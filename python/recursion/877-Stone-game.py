# Problem: Leetcode 877 - Stone game
# Difficulty: Medium
# Link: https://leetcode.com/problems/stone-game/description/
# Time Complexity: O(n^2) where n is the length of the array
# Space Complexity: O(n^2) for the memoization table
# Approach1: Use dynamic programming with memoization to calculate the maximum difference a player can achieve over their opponent in any subarray.
# Then we can return the list.
# Approach2: We can also use the fact that the first player can always win if they play optimally. This is because the first player can always choose the larger of the two ends of the array, and then the second player will be forced to choose from the remaining elements. This means that the first player will always have a higher score than the second player.
# this is because the total piles are even which means both get same number of piles and the sum of piles is odd which means the first player will always have a higher score than the second player if they choose optimally. so we can return true without any calculations

from rpds import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        '''
        recursive solution to check all
        @cache
        def dfs(left,right) -> int:
            if left>right:
                return 0
            choose_left = piles[left] - dfs(left+1,right)
            choose_right = piles[right] - dfs(left,right-1)
            return max(choose_left,choose_right)
        
        return dfs(0,len(piles)-1) > 0
        '''