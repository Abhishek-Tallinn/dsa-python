# Problem: Leetcode 3737 - Count subarray with majority element I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-subarrays-with-majority-element-I/description/
# Time Complexity: O(n^2) as we use nested loops
# Space Complexity: O(1) as we only usual store variables
# Approach: for each i we extend j and then for each j if nums[j] is target we keep extending cnt variable or if something diff from target then we decrement cnt ( like boyer moore voting algorithm)
# then for each j iteration we check if cnt>0 which means target is in majority in this subarray and if it is we increment ans.
# finally we return ans

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    cnt+=1
                else:
                    cnt-=1
                if cnt>0:
                    ans+=1
        return ans
                   