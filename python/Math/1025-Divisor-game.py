# Problem: Leetcode 1025 - Divisor game
# Difficulty: Easy
# Link: https://leetcode.com/problems/divisor-game/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We need to check the parity of move. If n is off any move forces the opponent to an even number based move as factors of odd n are only odd numbers
# and n-x will be odd. and then when its even you can do safe move of taking 1 which divides any n and force your opponent to make odd move. So since alice starts first
# if starting is odd alice can never win as as whatever moves she makes will give bob an even number due to the nature of the moves which dont preserve parity
# hence bob can make safe move and hand the odd number back to alice. However, if alice starts with even she can win for sure


class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2==0:
            return True
        return False