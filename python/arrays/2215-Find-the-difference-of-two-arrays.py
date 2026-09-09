# Problem: Leetcode 2215 - Find the difference of two arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We simply convert both into sets for quick look up and append the ones missing in the other set and return the answer
# Approach2: we can use set difference also as we only want element in the first second and not in second set from either side.
# the set difference approach gives us faster time complexity as it uses in built function instead of manual looping.

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1,n2 = set(nums1), set(nums2)
        return [list(n1-n2), list(n2-n1)]
        '''long method
        a1,a2 = [], []
        for num in n1:
            if num not in n2:
                a1.append(num)
        for num in n2:
            if num not in n1:
                a2.append(num)
        return [a1,a2]
        '''