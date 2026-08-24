# Problem: Leetcode 2529 - Maximum count of positive integer and negative integer
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We use binary searches to find the first positive and first negative index and calculate the max of both the numbers(negative and positive)
# for a smaller solution we can use bisect module.

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        first_pos = first_neg = None
        while left<=right:
            mid = (left+right)//2
            if nums[mid] > 0:
                first_pos = mid
                right = mid-1
            elif nums[mid] <= 0:
                left = mid+1
        left2=0
        right2=len(nums)-1
        while left2<=right2:
            mid = (left2+right2)//2
            if nums[mid] >= 0:
                right2 = mid-1
            elif nums[mid] < 0:
                first_neg = mid
                left2 = mid+1
        if first_neg is None and first_pos is None:
            return 0
        if first_neg is None:
            return len(nums)-first_pos
        if first_pos is None:
            return first_neg+1
        return max(first_neg+1,len(nums)-first_pos)   
      

        #return max(len(nums)-left, neg_index)
        
        '''
        pos = neg = 0
        mx = 0
        for num in nums:
            if num>0:
                pos+=1
            elif num<0:
                neg+=1
            mx = max(mx,pos,neg)
        return mx
        '''