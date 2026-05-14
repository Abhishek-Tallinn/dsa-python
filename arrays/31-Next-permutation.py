# Problem: Leetcode 31 - Next permutation
# Difficulty: Medium
# Link: https://leetcode.com/problems/next-permutation/description/
# Time Complexity: O(n) - as we go through all the elements of nums in worst case
# Space Complexity: O(1) as we dont use any additional data structure. slicing is amortized
# Approach: We use the usual method of finding the next higher permutation. we find the element which is the first time an element decreases.
# then we find its next higher element on its right side and replace them. then we reverse the remaining array
# also here we have to handle the cyclic case so if i == -1 which means its at the last permutation, then we just return nums.sort() which is first element in sorted permutations.

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i==-1:
            return nums.sort()
        # then we replace with the next higher
        j = len(nums)-1
        while nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j] = nums[j],nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return nums