# Problem: Leetcode 3471 - Find the largest almost missing integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/
# Time Complexity: O(n*k) we we go through the hashmap of the string
# Space Complexity: O(n) hashmap of 
# Approach1: we simply iterate over each subarray and take the unique element and update the count in our main hashmap
# at the end of loop only those keys with value 1 can be considered. from those keys we take the max value 

from collections import Counter
from typing import List
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = {}
        for i in range(len(nums)-k+1):
            temp = Counter(nums[i:i+k])
            for num in temp:
                d[num]=d.get(num,0)+1
        mx = -1
        for key,val in d.items():
            if val==1:
                mx = max(mx,key)
        return mx