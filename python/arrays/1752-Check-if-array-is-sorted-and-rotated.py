# Problem: Leetcode 1752 - Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) as we just check in the array
# Approach: Count the number of positions where an element is greater than the next element. If this count is 0, the array is sorted. If it's 1, the array is sorted and rotated. If it's more than 1, the array is not sorted and rotated.
# Approach2: Instead of count we can sort the array and try to find this sorted array in nums. For this we double the nums to make a circular array and then we slice and scan but this is O(log n) time complexity
# and space complexity goes up to O(n) as we double the array and also make slices. 

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        cnt=0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%n]: # if rotated properly it can only be count <=1
                cnt+=1
        return cnt<=1

        '''
        target = sorted(nums)
        cnums = nums+nums
        n = len(nums)
        for i in range(n):
            if cnums[i:i+n] == target:
                return True
        
        return False
        '''
            

        