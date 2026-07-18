# Problem: Leetcode 1979 - Minimum differnce between highest and lowest of k scores
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) 
# Approach: We simply sort the nums and then we slide a window and calculat the min possible difference.

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1 or k == 1:
            return 0
        #slide the window
        nums.sort()
        mn = float('inf')
        for right in range(len(nums)-k + 1):
            mn = min(mn,abs(nums[right]-nums[right+k-1]))

        return mn