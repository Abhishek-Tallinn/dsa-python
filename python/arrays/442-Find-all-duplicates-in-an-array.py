# Problem: Leetcode 442 - Find all duplicates in an array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We use the fact that the numbers are mean to be from 1 to n. So any duplicate will shadow a number. We use cyclic sort to get numbers in their correct positions.
# The duplicates will not be able to shuffle because the first copy of the number would havem moved into the correct position first
# Hence duplicates would be stuck in wrong index. then we iterate over the sorted array and coolect the values which are not at index + 1.

# Appraoch2: is O(n) and O(n) where we just use a set and collect duplicates.

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(len(nums)):
            while nums[i]!=nums[nums[i]-1]:
                correct_index = nums[i]-1
                nums[correct_index],nums[i] = nums[i],nums[correct_index]
        duplicates = []
        for i,num in enumerate(nums):
            if num!=i+1:
                duplicates.append(num)
        return duplicates

        '''
        simple but using set
        s = set()
        res = []
        for num in nums:
            if num in s:
                res.append(num)
            s.add(num)
        return res
        '''