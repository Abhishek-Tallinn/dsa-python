# Problem: Leetcode 292 - Nim Game
# Difficulty: Easy
# Link: https://leetcode.com/problems/nim-game/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: The key insight is that if the number of stones is a multiple of 4, the current player will lose if both players play optimally. Otherwise, the current player will win.
# The solution can be optimized further by directly checking that n is a multiple of 4 or not, but this is the initial solution i wrote.
# We are checking if after taking 1 or 2 or 3 stones, the opponent is left with a multiple of 4. If yes, then we can win the game. Else, we will lose the game.


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3:
            return True
        if (n-1)%4==0 or (n-2)%4==0 or (n-3)%4==0:
            return True
                   
        return False
    