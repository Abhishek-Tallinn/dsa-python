# Problem: Leetcode 349 - Intersection of Two Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-arrays/description/
# Time Complexity: O(n + m) where n and m are the lengths of the two arrays
# Space Complexity: O(min(n, m)) for storing the smaller array in a set
# Approach: Convert the smaller array to a set and iterate through the larger array, adding elements to the result if they exist in the set.
# Therefore the result will only contain unique elements.


from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        nums2 = set(nums2)
        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)

        return list(ans)