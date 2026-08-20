# Problem: Leetcode 3523 - Make array non decreasing
# Difficulty: Medium
# Link: https://leetcode.com/problems/make-array-non-decreasing/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use a stack
# Approach: Since we have to acheive monotonic condition and also elements have to be dropped the sliding window fails here.
# we keep a stack and keep dropping elements if they dont satisfy the value. When the answer is len of the elements kept then 
# usually we use stack approach.

from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if stack and stack[-1] > num:
                continue
            stack.append(num)
        return len(stack)