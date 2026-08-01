# Problem: Leetcode 75 - Sort colors
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-colors/description/
# Time Complexity: O(n) - we do one pass with dutch national flag
# Space Complexity: O(1) as no additional data structure is used.
# Approach: We keep three pointers to avoid multiple pass. low to track 0, mid for 1 and high for 2.
# mid traverses array and if mid finds a 0, we swap with low and increment both low and mid.
# if mid finds 1 then we just incremnet mid and if its finds 2 then we swap with high position and only decrement high pointer


from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch flag
        low = 0
        mid = 0
        high = len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1

        '''
        my own solution - O(n) with 2 passes
        left = 0
        target = 0
        while left<len(nums)-1:
            while left+1<len(nums) and nums[left] == target:
                left+=1
            for right in range(left+1,len(nums)):
                if nums[right] == target:
                    nums[left],nums[right] = nums[right],nums[left]
                    left+=1 #left only shoud increment when interchange done
            #loop over
            target += 1
        '''