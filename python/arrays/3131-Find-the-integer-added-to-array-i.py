# Problem: Leetcode 3131 - Find the Integer Added to Array I
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
# Time Complexity: O(n) where n is the number of elements in the arrays.
# Space Complexity: O(1) as not extra space i used
# Approach: The difference between the minimum elements of the two arrays gives the integer added to nums1 to get nums2. 
# as the integer added to each element 'x' is same the minimum of nums1 will convert to minimum eleement of nums2


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
        