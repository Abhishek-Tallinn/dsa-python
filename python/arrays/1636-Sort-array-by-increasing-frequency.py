# Problem: Leetcode 1636 - Sort array by increasing frequency
# Difficulty: Easy
# Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(n) due to dictionary
# Approach1: sort the original list but pass a custoemr function that return the dictionary freq count and other by num in decreasing order
# Appraoch2: we make a freq hashmap and then sort the hashmap via lambda function as key can take only one callable.
# then we reconstruct the answer list from the final sorted dictionary

from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        def sort_func(n):
            return (d[n],-n)
        nums.sort(key = sort_func)
        return nums 
        '''
        d = Counter(nums)
        s_d = dict(sorted(d.items(),key=lambda x:(x[1],-x[0])))
        res = []
        for key,value in s_d.items():
            temp = [key]*value
            res.extend(temp)
        return res
        '''