#Problem: Leetcode 2974 - Minimum number game
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-number-game/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) as we have answer array
# Approach: We sort nums in reverse so min number can be found in O(1) time for alice and pop. THen we pop twice
# to get the two minimum numbers in one move and append them in the order bob and alice and finally we return ans.

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort(reverse=True)
        n = len(nums)
        while len(arr)<n:
            alice = nums.pop()
            bob = nums.pop()
            arr.extend([bob,alice])
        return arr