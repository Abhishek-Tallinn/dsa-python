# Problem: Leetcode 2295 - Replace elements in an array
# Difficulty: Medium
# Link: https://leetcode.com/problems/replace-elements-in-an-array/description/
# Time Complexity: O(n) as we make multiple separate O(n) loops
# Space Complexity: O(n) 
# Approach: We make two hashmaps one mapping index to number which will hold final values. second hashmaps maps the number to its index.
# when operation comes which replaces one number with another, we first use the second hashmap to find the index of this number in array 3
# and then replace the first hashmap value with new number. But since now this is a new number we have to add its index into our second hashmap for future look ups.
# this gives O(1) look ups per query

from collections import Counter
from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {idx:num for idx,num in enumerate(nums)}
        t = {num:idx for idx,num in enumerate(nums)}
        for op in operations:
            target_idx = t[op[0]]
            d[target_idx] = op[1]
            t[op[1]] = target_idx
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = d[i]
        return ans