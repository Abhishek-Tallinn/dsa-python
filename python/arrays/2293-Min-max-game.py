# Problem: Leetcode 2293 - Min max game
# Difficulty: Easy
# Link: https://leetcode.com/problems/min-max-game/description/
# Time Complexity: O(n*n//2) as we half the space each time 
# Space Complexity: O(n) as we create new Nums
# Approach: We keep populating newNums as per the logic and keep appending values to it.

from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            newNums = []
            for i in range(0,len(nums)//2):
                if i%2==0:
                    newNums.append(min(nums[2*i], nums[2*i+1]))
                else:
                    newNums.append(max(nums[2*i], nums[2*i+1]))
            nums = newNums
        return nums[0]