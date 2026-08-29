# Problem: Leetcode 2363 - Number of arithmetic triplets
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-arithmetic-triplets/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we use a set
# Approach: Since each number of unique in increasing order and there can be no duplication
# we can for each number in nums checks if its diff and 2*diff which are both needed to make a triplet are in the set.
# set is set(nums) which is needed for O(1) look up

from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        cnt = 0
        for num in nums:
            if num+diff in s and num+2*diff in s:
                cnt+=1
        return cnt
        '''
        brute force O(n^3) solution
        cnt = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[j]-nums[i] == diff and nums[k]- nums[j]==diff:
                        cnt+=1
        return cnt
        '''