# Problem: Leetcode 594 - Longest harmonious subsequence
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-harmonious-subsequence/description/
# Time Complexity: O(n log n) due to sorting, where n is the number of scores
# Space Complexity: O(n) for the dictionary and result list
# Approach: We sort the array and use a sliding window technique to find the longest harmonious subsequence.
# After sorting we keep increasing window size and if diff between right and left is 1 then we update our mx varible length
# and if diff is greater than 1 we keep moving left pointer till we get diff of 1 or less. We return the mx length at the end.


from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        if nums[0] == nums[-1]:
            return 0
        if nums[-1]-nums[0]==1:
            return len(nums)
        left = 0
        for right in range(len(nums)):
            while left<right and nums[right]-nums[left]>1:
                left+=1
            if nums[right] - nums[left]==1:
                mx = max(mx,right-left+1)
        return mx 