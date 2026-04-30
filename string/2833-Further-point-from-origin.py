# Problem: Leetcode 2833 - Furthest Point from Origin
# Difficulty: Easy
# Link: https://leetcode.com/problems/furthest-point-from-origin/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Straighforward approach to keep track of balance variable and add empty count to which direction has more weight.


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        balance = empty_count = 0
        for char in moves:
            if char == 'L':
                balance-=1
            elif char == 'R':
                balance+=1
            else:
                empty_count+=1

        return abs(balance) + empty_count