# Problem: Leetcode 88 - Merge sorted array
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-sorted-array/description/
# Time Complexity: O(n) - we do a two pointer based merging in sequence
# Space Complexity: O(1) as no additional data structure is used.
# Approach: We keep a write pointer k and then we keep writing values from the array which is larger to 
# keep the array sorted. Its a good example of two pointer based sorting

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n - 1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1