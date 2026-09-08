# Problem: Leetcode 1413 - Minimum value to get positive step by step sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We keep a running sum and at the end we check that if we did not drop lower than 1 then we just return 1 as we have to return a positive value
# otherwise if we dropped to a negative value, we return its positive inverse + 1

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = float('inf')
        rolling_sum = 0
        for num in nums:
            rolling_sum+=num
            mn = min(mn,rolling_sum)
        return 1 if mn>=1 else abs(mn)+1