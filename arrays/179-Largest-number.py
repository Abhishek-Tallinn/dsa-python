# Problem: Leetcode 179 - Largest Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/largest-number/description/
# Time Complexity: O(n log n) - as we are sorting the list
# Space Complexity: O(n) as we restore the result after sorting 
# Approach: We convert eacah element of nums from int to str and then sort them using the compare function with the cmp_to_key inbuilt function that wraps a function so that it can be used in key sorting argument.
# We only check at the end that if there are multiple 0s then return 0 else we return the result


from typing import List

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            if a+b>b+a:
                return 1
            elif a+b<b+a:
                return -1
            else:
                return 0

        nums = list(map(str,nums))
        nums.sort(key = cmp_to_key(compare), reverse = True)
    
        res =  ''.join(nums)

        return '0' if res[0]=='0' else res