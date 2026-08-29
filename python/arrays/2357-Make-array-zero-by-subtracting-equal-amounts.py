# Problem: Leetcode 2357 - Minimum array zero by subtracting equal elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-elements/description/
# Time Complexity: O(n log n) as we sort the cost array in reverse
# Space Complexity: O(1) as no extra data structure is used
# Approach: We just count number of unique values except 0 in array as all would need one operation to be reduced to zero
# and that would be the total operations.

from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        cnt=0
        for key in d.keys():
            if key==0:
                continue
            cnt+=1
        return cnt
        '''
        iterative solution
        nums.sort(reverse=True)
        ops = 0
        while nums and nums[-1]==0:
                nums.pop()
        
        while sum(nums)!=0:
            while nums and nums[-1]==0:
                nums.pop()
            mn = nums.pop()
            for i in range(len(nums)):
                nums[i]-=mn
            ops+=1
        return ops
        '''