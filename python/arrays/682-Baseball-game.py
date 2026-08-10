# Problem: Leetcode 682 - Baseball game
# Difficulty: Easy
# Link: https://leetcode.com/problems/baseball-game/description/
# Time Complexity: O(n) as we iterate through the operations once
# Space Complexity: O(n) as we use a stack to store the scores
# Approach: We iterate through the operations and apply the rules to update the stack of scores.

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:

            if op=='+':
                stack.append(stack[-1]+stack[-2])
            elif op=='D':
                stack.append(stack[-1]*2)
            elif op=='C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)