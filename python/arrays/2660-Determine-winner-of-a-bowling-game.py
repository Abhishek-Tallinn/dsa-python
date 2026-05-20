# Problem: Leetcode 2660 - Determine Winner of a Bowling Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/determine-winner-of-a-bowling-game/description/
# Time Complexity: O(n) - as we go over the scores in the array.
# Space Complexity: O(1)
# Approach: Since both players play the same game and score calculation logic is same we use a helper function as an API to return the scores of players.
# Then we compare the and return the answer.

from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(player):
            total = 0
            for i in range(len(player)):
                if (i>0 and player[i-1]==10) or (i>1 and player[i-2]==10):
                    total+=2*player[i]
                else:
                    total+=player[i]
            return total
        score_1 = score(player1)
        score_2 = score(player2)
        if score_1>score_2:
            return 1
        elif score_1<score_2:
            return 2
        
        return 0
   