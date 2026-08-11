# Problem: Leetcode 760 - Find Anagram Mappings
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-anagram-mappings/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we store the mapping
# Approach: Create a mapping from elements in nums2 to their indices, then use this mapping to create the result for nums1.
# the best path is not acheived by making greedy solution.

from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = [0]*len(nums1)
        map2 = {num:i for i,num in enumerate(nums2)}
        for i,num in enumerate(nums1):
            mapping[i] = map2[num]
        return mapping