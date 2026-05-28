# Problem: Leetcode 217 - Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(n) as we store elements in a set. O(k) if duplicate found earlier
# Approach: We use a set to keep track of elements we have seen. If we encounter an element that is already in the set, we return True. If we finish the loop without finding duplicates, we return False.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False