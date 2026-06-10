# Problem: Leetcode 1099 - Two Sum Less Than K
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum-less-than-k/description/
# Time Complexity: O(n log n) - due to sorting
# Space Complexity: O(log n) to O(n) - due to the sorting algorithm
# Approach: Sort the array and use two pointers to find the maximum sum less than k.
# We iterate with two pointers from both sides and keep increasing the total as long as its less than k and keeping increasing the max value seen.


from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        mx = 0
        if k ==1:
            return -1
        while i < j:
            if nums[i] + nums[j] < k:
                mx = max(mx,nums[i]+nums[j])
                i+=1
            else:
                j-=1
        return mx if mx else -1