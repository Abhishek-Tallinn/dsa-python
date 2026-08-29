#Problem: Leetcode 2970 - Count the number of incremovable subarrays I
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/
# Time Complexity: O(n) as we loop twice on array
# Space Complexity: O(1) as we only use pointers
# Approach: We take left boundary forwards upto the strictly increasing point.If it reaches the end we know array is sorted and we return all the subarrays
# which is represented by n*(n+1)//2. Else we add left boundary + 2 subarrays as that how much we can remove to keep it sorted.
# then we take right boundary and move it inwards. we move left boundary till its bigger than right boundary and taken the index + 2 subarrays
# which we can again remove. If right boundary reaches a point where a number of left is increasing then 
# If right boundary reaches the deflection point we just stop the algorithm and we return our result.

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        left_boundary = 0
        n = len(nums)
        while left_boundary +1 < n and nums[left_boundary] < nums[left_boundary+1]:
            left_boundary+=1 
        if left_boundary == n-1:
            return (n*(n+1))//2
        res = left_boundary+2
        right_boundary = n-1
        while right_boundary>0:
            while left_boundary>=0 and nums[left_boundary] >= nums[right_boundary]:
                left_boundary-=1 
            print("current_left",left_boundary)
            res += left_boundary+2
            if nums[right_boundary-1] >= nums[right_boundary]:
                break
            right_boundary-=1
        return res