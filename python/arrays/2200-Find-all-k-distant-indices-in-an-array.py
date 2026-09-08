# Problem: Leetcode 2200 - Keep multiplying found values by 2
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Approach: We simply track the indices where key exists first. We can add them in hashmap too but the input size is small
# so look up in a list which is O(n) will also work. Then we loop the array and check in nested loop if the current index has any key indices 
# for which the absolute value of diffence is less than 1. If yes we append and break immediately to check next index.

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []
        ans = []
        for i,num in enumerate(nums):
            if num == key:
                indices.append(i)
        for i in range(len(nums)):
            for idx in indices:
                if abs(i-idx) <= k:
                    ans.append(i)
                    break
        return sorted(ans)