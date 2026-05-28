# Problem: Leetcode 219 - Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(n) as we store elements in a set. O(k) if duplicate found earlier
# Approach: We use a dictionary to store the indices of elements we have seen. If we encounter an element that is already in the dictionary and the difference in indices is less than or equal to k, we return True. If loop end we return False.


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = {}
        for idx,num in enumerate(nums):
            if num in d and abs(d[num] - idx) <= k:
                return True
            d[num] = idx
        return False