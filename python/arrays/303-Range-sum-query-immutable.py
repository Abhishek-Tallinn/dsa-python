# Problem: Leetcode 303 - Range sum query immutable
# Difficulty: Easy
# Link: https://leetcode.com/problems/range-sum-query-immutable/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(1) as we are modifying the list in-place
# Approach: We simply calculate prefix sum array before any sumrange calls to have O(1) time complexity for each call
# to sumrange instead of the usual O(k) calls

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [self.nums[0]]
        for i in range(1,len(self.nums)):
            self.prefix.append(self.prefix[-1] + self.nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)