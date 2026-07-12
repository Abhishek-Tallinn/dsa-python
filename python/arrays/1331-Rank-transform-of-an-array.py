# Problem: Leetcode 1331 - Rank transform of an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/rank-transform-of-an-array/description/
# Time Complexity: O(n log n) due to sorting 
# Space Complexity: O(n) as we use a dictionary and a list
# Approach: We remove duplocates and sort the array and make a hashmap of the rank of each element
# then we iterate over original array we append its rank from the hashmap to our answer array.

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s_arr = list(set(tuple(arr)))
        s_arr = sorted(s_arr)
        rank_d = {}
        for idx,num in enumerate(s_arr):
            if num not in rank_d:
                rank_d[num] = idx+1
        ans = []
        for num in arr:
            ans.append(rank_d[num])
        return ans