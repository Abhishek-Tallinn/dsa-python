# Problem: Leetcode 2210 - Count hills and valleys in an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We simply loop the array and check if a number is bigger than its previous index then we want to check its next element to check if its a hill 
# and similarly vice versa for valley but only difference is that in both branches we add a check to loop over the repeated values
# as the hills or valley can be created beyond the repetition. If after skiiping repeats there is still a hill or valley condition we increment
# our count pointer

from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        cnt = 0
        while i < len(nums)-1:
            if nums[i] > nums[i-1]:
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i+=1
                if i+1< len(nums) and nums[i] > nums[i+1]:
                    cnt+=1
            elif nums[i] < nums[i-1]:
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i+=1
                if i+1<len(nums) and nums[i] < nums[i+1]:
                    cnt+=1
            
            i+=1
               
        return cnt   