# Problem: Leetcode 645 - Set mismatch
# Difficulty: Easy
# Link: https://leetcode.com/problems/set-mismatch/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) 
# Approach: We convert to hashmap and find the repeating value. then we run a loop of ideal numbers from 1 to n
# and find the value which is missing in d and immediately return the answer

from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        d = Counter(nums)
        target = 0
        for key,value in d.items():
            if value==2:
                target = key
        for i in range(1,len(nums)+1):
            if i not in d:
                return [target,i]