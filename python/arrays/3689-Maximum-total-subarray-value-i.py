# Problem: Leetcode 3689 - Maximum Total Subarray Value I
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-total-subarray-value-i/description/
# Time Complexity: O(n) as we calculate max and min and O(n) + O(n) is O(n)
# Space Complexity: O(1) as we only use a constant amount of extra space.
# Approach: Since any subarray is possible we just keep taking the maximum subarray k time and return the answer.

from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums)-min(nums))*k