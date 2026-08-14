# Problem: Leetcode 260- Single Number III
# Difficulty: Medium
# Link: https://leetcode.com/problems/single-number-III/description/
# Time Complexity: O(n)
# Space Complexity: O(1) for xor and O(n) for hashmap
# Approach: we can use simple hashmap and then count elements with freq of 1 but we can also use the XOR approach which is still
# O(n) time complexity but the space is reduced to O(1)

from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #xor trick
        xor = 0
        for num in nums:
            xor^=num
        #diff bit
        diff_bit = xor&(-xor)
        a=b=0
        for num in nums:
            if num&diff_bit:
                a^=num
            else:
                b^=num
        return [a,b]
        '''
        hashamp O(n) and O(n)
        ans = []
        d = Counter(nums)
        for val,freq in d.items():
            if freq==1:
                ans.append(val)
        return ans
        '''