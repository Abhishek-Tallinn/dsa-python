# Problem: Leetcode 162 - Find peak element
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-peak-element/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: Simple binary search over the array where we follow the direction based binary search. if mid is greater than mid+1 then peak must be to the left and we set right to mid.
# otherwise is mid element < mid+1 the peak must be at the right so we set right = mid


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #check edge cases first to find answer fast
        left , right = 0 , len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
        '''manual solution for exact peak
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if mid >0 and nums[mid]>nums[mid-1] and mid+1<len(nums) and nums[mid]>nums[mid+1]:
                return mid
            elif mid >0 and nums[mid]<nums[mid-1]:
                right = mid-1
            else:
                left = mid+1
        '''