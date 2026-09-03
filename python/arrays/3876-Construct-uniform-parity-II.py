# Problem: Leetcode 3876 - Construct uniform parity array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/construct-uniform-parity-array-ii/description/
# Time Complexity: O(n) as we do two loops on array
# Space Complexity: O(1)
# Approach: We check if array already odd or even and return True if it is. If it has both even and odd elements then based on the subtraction operations
# we can only make the array odd. So we keep track of minimum odd element during second loop we only check 
# if for any even element that we find, we have that even element equal or less than the minimum odd element and then the condition breaks and we return False
# if loop finishes successfully then we return True as all evens can be changed to odd elements.

from typing import List

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odds=0
        odd_min = float('inf')
        for num in nums1:
            if num%2==1:
                odds+=1
                odd_min = min(odd_min,num)
        if odds ==0 or odds == len(nums1):
            return True
        #check if evens can be changed
        for num in nums1:
            if num%2==0:
                if num - odd_min < 1:
                    return False
        return True