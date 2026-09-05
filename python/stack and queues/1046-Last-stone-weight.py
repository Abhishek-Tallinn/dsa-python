# Problem: Leetcode 1046 - Last stone weight
# Difficulty: Easy
# Link: https://leetcode.com/problems/last-stone-weight/description/
# Time Complexity: O(1) as we only append and pop to stack
# Space Complexity: O(n) as we have to use a stack
# Approach: since we always have to take the heaviest stones we sort the array and take the top two element.
# if both equal meaning both will be destroyed then we just continue to next iteration otherwise if first > second 
# we append first-second to the stones stack again and immediately sort it to take the biggest two weight in next iteration

from bisect import bisect_left
from collections import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            first = stones.pop()
            second = stones.pop()
            if first == second:
                continue
            elif second < first:
                stones.append(first-second)
                stones.sort()
        return stones[0] if stones else 0