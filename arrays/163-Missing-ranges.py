# Problem: Leetcode 163 - Missing ranges
# Difficulty: Easy
# Link: https://leetcode.com/problems/missing-ranges/description/
# Time Complexity: O(n) - as we go through all the element of nums
# Space Complexity: O(n) as we are producing answer array
# Approach: Simple appraoch with handling lower bound and upper bound edge cases separately of the loop.
# Inside the loop we just check if the diff between two consecutive numbers is >1 and if it is we append the missing range to the answer list and return it

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]: 
        if not nums:
            return [[lower,upper]]
        ans= []
        if nums[0]!=lower:
            ans.append([lower,nums[0]-1])
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-start >1:
                ans.append([start+1,nums[i]-1])
            start = nums[i]
        if nums[-1]<upper:
            ans.append([nums[-1]+1,upper])
        return ans
            