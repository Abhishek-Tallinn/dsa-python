# Problem: Leetcode 1248 - Count number of nice subarrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) due to hashmap
# Approach: We make a hashmap and add the odd_counts in our hashmap to create prefix array and 
# we keep an odd cnt as we go through the array and keep adding the hashmap value of odd_cnt - k. Ex. if we have seen 4 odd numbers
# then we want to add hashmap value of prefix_count[4-1] to the result as we will subtract the number of subrrays 
# which have odd_cnt as 1. The remaining subarrays will exactly have an odd cnt of k.


from collections import defaultdict
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0
        odd_cnt = 0
        for num in nums:
            odd_cnt += num%2
            result += prefix_count[odd_cnt-k]
            prefix_count[odd_cnt]+=1
        return result
        '''
        O(n^2) solution - TLE
        total_cnt = 0
        for i in range(len(nums)):
            odd_cnt = 0
            for j in range(i,len(nums)):
                if nums[j]%2==1:
                    odd_cnt+=1
                if odd_cnt == k:
                    total_cnt+=1
        return total_cnt
        '''