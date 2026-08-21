# Problem: Leetcode 3507 - Minimum pair removal to sort array I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/
# Time Complexity: O(n^2 log n) 
# Space Complexity: O(n)
# Approach: We loop till nums!=sorted(nums) and keep finding the leftmost index and replacing nums with new nums without the two dropped elements and
# replacing them with their sum.


from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops=0
        if nums==sorted(nums):
            return 0
        while nums!=sorted(nums):
            if len(nums)==1:
                return ops
            mn = float('inf')
            target_index = -1
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < mn:
                    mn = nums[i] + nums[i+1]
                    target_index = i
            nums = nums[:target_index] + [mn] + nums[target_index+2:]
            ops+=1
        return ops
        '''
        ops = 0
        while True:
            if len(nums)==1:
                return ops
            mn = float('inf')
            target_index = -1
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < mn:
                    mn = nums[i] + nums[i+1]
                    target_index = i
            copy = []
            for i in range(len(nums)):
                if i == target_index:
                    copy.append(mn)
                    ops+=1
                elif i == target_index+1:
                    continue
                else:
                    copy.append(nums[i])
            if copy==sorted(copy):
                return ops
            nums = copy
            
        return ops
        '''
        