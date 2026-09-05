# Problem: Leetcode 1052 - Grumpy bookstore owner
# Difficulty: Medium
# Link: https://leetcode.com/problems/grumpy-bookstore-owner/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We calculate the total already safisfied customers and then use prefix sum where the prefix sum
# is based on those values when is owner is grumpy and excludes values when he is non grumpy so that the window 
# only has gains in it the effective gain. then we just iterate over the window and check the mx gain possible
# then we return the original satisfied customers + max gain 

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #satisfied = sum(c for c,g in zip(customers,grumpy) if not g)
        satisfied = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                satisfied+=customers[i]
        prefix = [0]*(len(customers)+1)
        for i in range(len(customers)):
            prefix[i+1] = prefix[i] + (customers[i] if grumpy[i] else 0)
    
        mx = 0
        for i in range(len(grumpy)-minutes+1):
            mx  = max(mx, prefix[i+minutes] - prefix[i]) 
        return satisfied + mx

         '''
        rolling sum space O(1) optimization
        satisfied = sum(c for c, g in zip(customers, grumpy) if not g)
        
        window = sum(customers[i] for i in range(minutes) if grumpy[i])
        best = window
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                window += customers[i]
            if grumpy[i - minutes]:
                window -= customers[i - minutes]
            best = max(best, window)
        
        return satisfied + best
        '''