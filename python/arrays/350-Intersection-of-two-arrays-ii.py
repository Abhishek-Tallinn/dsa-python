# Problem: Leetcode 350 - Intersection of Two Arrays II
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# Time Complexity: O(n log n + m log m) where n and m are the lengths of the two arrays as we sort them
# Space Complexity: O(1) as we only sort the array in place. but python in place sort uses some memory so we can say O(n + m) in worst case
# Approach: Sort the two arrays and use two pointers to iterate over them. if the value is equal then we write it to our result and increment both pointers. if not then we just do see which value is smaller and increment that pointer. We continue this until we reach the end of one of the arrays. This way we get all the common elements in both arrays including duplicates as well.
# else we just do see which value is smaller and increment that pointer.

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=j=0
        ans = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return ans
