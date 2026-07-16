# Problem: Leetcode 229 - Majority Element II
# Difficulty: Medium
# Link: https://leetcode.com/problems/majority-element-ii/description/
# Time Complexity: O(n) - as we are iterating through the list once
# Space Complexity: O(n) as we have a hashmap
# Approach: We make a hashmap and check the freqeuencies to collect elements which meet our criteria

from typing import List 
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d = Counter(nums)
        n = len(nums)
        ans = []
        for num,count in d.items():
            if count>n//3:
                ans.append(num)
        return ans
        

        # can do it slower in time but in O(1) space with boyer-moore
        # voting algorithm