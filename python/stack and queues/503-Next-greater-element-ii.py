# Problem: Leetcode 503 - Next greater element- II
# Difficulty: Medium
# Link: https://leetcode.com/problems/next-greater-element-ii/description/
# Time Complexity: O(n) as we iterate through the list
# Space Complexity: O(n) 
# Approach1: We maintain a monotonic stack as in case of next greater element 1 but this time we loop twice so that the digits at end also get a chance
# to see the elements before them and we check stack and array with modulo index
# Approach2: We are brute forcing. we double the list and check the elements upto the length of original nums for each element and if a greater
# one is found we append it and break

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        n = len(nums)
        stack = []
        for i in range(n*2-1,-1,-1):
            index = i%n
            while stack and stack[-1] <= nums[index]:
                stack.pop()
            if stack:
                res[index] = stack[-1]
            stack.append(nums[index])
        return res

        '''
        Brute force O(n^2) - as 10^4 allows it - passes
        nge2 = [-1]*len(nums)
        nums = nums+nums
        
        for i in range(len(nums)//2):
            j = i+1
            while j+1<len(nums) and j-i< len(nums):
                if nums[j]>nums[i]:
                    nge2[i] = nums[j]
                    break
                j+=1
        return nge2
        '''