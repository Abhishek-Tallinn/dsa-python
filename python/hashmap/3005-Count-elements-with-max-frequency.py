# Problem: Leetcode 3005 - Count Elements with Maximum Frequency
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
# Time Complexity: O(n) as we go through the array once
# Space Complexity: O(n) as we use the dictionary data structure
# Approach1: We find the maximum value and then just find the total count of the maximum value in the array and return it.

from typing import List

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        max_freq = max(freq_map.values())
        cnt = 0
        for key,value in freq_map.items():
            if value == max_freq:
                cnt +=value
        return cnt