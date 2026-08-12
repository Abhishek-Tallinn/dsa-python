#Problem: Leetcode 2958 - Length of longest subarray with at most k frequency
# Difficulty: Medium
# Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
# Time Complexity: O(n) - as we use sliding window
# Space Complexity: O(n) as we use a hashmap
# Approach: Simply iterate over the array while keeping the window valid where all window element have freq
# <=k by storing this in a hashmap. If window become invalid at current element we push left pointer 
# till it becomes valid again. At each step we keep taking length of current window to find the maximum

from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        d = defaultdict(int)
        longest = 0
        for right in range(len(nums)):
            d[nums[right]]+=1
            while left < right and d[nums[right]]>k:
                d[nums[left]]-=1
                left+=1
            longest = max(longest,right-left+1)
        return longest