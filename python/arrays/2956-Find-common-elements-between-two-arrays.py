# Problem: Leetcode 2956 - Find common elements between two arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-common-element-between-two-arrays/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use two sets for quick look up
# Approach: We make set of both arrays to look up in O(1) time. then we iterate both arrays and increment 
# answer1 and answer2 to see how many elements are common.

from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1= set(nums1)
        s2=set(nums2)
        answer1 = answer2 = 0
        answer1 = sum(1 for num in nums1 if num in s2)
        answer2 = sum(1 for num in nums2 if num in s1)
        return [answer1,answer2]