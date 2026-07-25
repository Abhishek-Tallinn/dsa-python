# Problem: Leetcode 496 - Next greater element
# Difficulty: Easy
# Link: https://leetcode.com/problems/next-greater-element-i/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make hashmap
# Approach: We make NGE array of nums2 and convert it to hashmap for fast look up of nums1 element. 

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = []
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            nge.append(-1 if not stack else stack[-1])
            stack.append(nums2[i])
        nge.reverse()
        d = {}
        for i,num in enumerate(nums2):
            d[num] = nge[i]
        ans = []
        for num in nums1:
            ans.append(d[num])
        return ans