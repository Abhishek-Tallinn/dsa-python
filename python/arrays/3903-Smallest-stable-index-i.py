# Problem: Leetcode 3903 - Smallest Stable Index I
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-stable-index-i/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we use prefix and suffix array
# Approach: We create prefix and suffix array in one loop and then use it to check if difference at any index is <= k.
# if yes then we immediately take that index and break as we need the smallest index and we return -1.

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        smallest_stable_index = -1
        prefix_mx =  [nums[0]]
        suffix_mn = [nums[-1]]
        for i in range(1,len(nums)):
            prefix_mx.append(max(prefix_mx[-1],nums[i]))
            suffix_mn.append(min(suffix_mn[-1],nums[len(nums)-i-1]))
        suffix_mn = suffix_mn[::-1]
        for i in range(len(nums)):
            if prefix_mx[i] - suffix_mn[i] <= k:
                smallest_stable_index = i
                break
        return smallest_stable_index 