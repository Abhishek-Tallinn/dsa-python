# Problem: Leetcode 560 - Subarray sum equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Time Complexity: O(n) as we go through the array once
# Space Complexity: O(n) as we use the dictionary data structure
# Approach1: We initialize a default dict of int and add prefix_sum[0]=1 which is used as base case that we have seen prefix sum of 0 exactly one time. Without this the algorithm will fail.
# Then we keep adding prefix sum to our hashmap for value current_sum-k to increase count of the subarrays that have sub as k.


from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0]=1
      
        result = 0 # this counts the number of arrays
        current_sum = 0 #this is running sum
      
        # Iterate through each number in the array
        for num in nums:
            
            current_sum += num
          
            # Check if (current_sum - k) exists in our hash map
            # If yes then subarray exist at the current level
         
            result += prefix_sum_count[current_sum - k]
          
            # Add current sum for future iterations
            
            prefix_sum_count[current_sum] += 1
        
      
        return result