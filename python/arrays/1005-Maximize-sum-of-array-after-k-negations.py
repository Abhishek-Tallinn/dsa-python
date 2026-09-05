# Problem: Leetcode 1005 - Maximize sum of array after k negations
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
# Time Complexity: O(n log n) as we sort
# Space Complexity: O(1)
# Approach: we sort the numbers and want to use each k once to flip each negative to a positive
# then when we reach boundary of negative and positive we make a decision where to exhause them on last negative
# or carry over to next positive it that brings more gain to us. This will make the largest array
# and we return the sum of this array

from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k % 2 == 1:
            nums.sort()  # re-sort since flipping may have changed order
            nums[0] = -nums[0]
        return sum(nums)
        '''
        nums.sort()
        target_idx = None
        for i in range(len(nums)):
            if nums[i] > 0:
                target_idx = i
                break
        if target_idx is None:
            target_idx = len(nums)
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i]<0 and i+1 == target_idx:
                if k%2==1:
                    nums[i] = -nums[i]
                    break
                elif k%2==0:
                    if i+1< len(nums) and abs(nums[i]) > abs(nums[i+1]):
                        nums[i]=-nums[i]
                        k=1
                    else:
                        break
            elif nums[i] <0:
                nums[i] = -nums[i]
                k-=1
            elif nums[i]>=0:
                if k%2==1:
                    nums[i]=-nums[i]
                    break
    
        return sum(nums)
        '''
        