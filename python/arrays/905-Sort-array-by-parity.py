# Problem: Leetcode 905 - Sort array by parity
# Difficulty: Easy
# Link: https://leetcode.com/problems/sort-array-by-parity/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: we take two pointer approach and keep moving then towards each other and swtiching at the point where left is odd and right is an even number.
# this is standard approach for such questions

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left]%2==0:
                left+=1
            elif nums[right]%2==1:
                right-=1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        return nums