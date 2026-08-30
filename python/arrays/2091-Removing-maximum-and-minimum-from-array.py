# Problem: Leetcode 2091 - Removing maximum and minimum from array
# Difficulty: Medium
# Link: https://leetcode.com/problems/removing-maximum-and-minimum-from-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Input size allows us to take the index of both elements direcltly in O(n) and all elements being distinct
# also helps. Then we can check if to remove both elements from one side or both from the other side 
# or to remove one element from each side 

from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        #bruting
        n = len(nums)
        if n == 1:
            return 1
        mx_index = nums.index(max(nums))
        mn_index = nums.index(min(nums))
        if mx_index<=n//2 and mn_index<=n//2:
            return max(mx_index+1,mn_index+1)
        elif mx_index>=n//2 and mn_index>=n//2:
            return max(n-mn_index,n-mx_index)
        else:
            if mx_index>=n//2 and mn_index<=n//2:
                return min(n-mx_index+mn_index+1,mx_index+1,n-mn_index) 
            elif mx_index<=n//2 and mn_index>=n//2:
                return min(mx_index+1+n-mn_index, mn_index+1,n-mx_index) 