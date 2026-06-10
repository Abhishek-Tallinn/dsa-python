# Problem: Leetcode 283 - Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(1) as we are modifying the list in-place
# Approach: We use two pointers to efficiently move all zeros to the end of the list while maintaining the relative order of non-zero elements. The left 
# pointer keeps track of the next position where a non zero element should be placed, and the right pointer find that non zero element and then we switch them.


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
        return nums
        '''
        while right<len(nums):
            if left==right:
                right+=1
            elif nums[left]!=0:
                left+=1
            elif nums[right]==0:
                right+=1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right+=1
        return nums
        '''
        