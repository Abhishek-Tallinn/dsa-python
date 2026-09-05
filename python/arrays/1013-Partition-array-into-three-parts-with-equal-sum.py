# Problem: Leetcode 1013 - Partition array into three parts with equal sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: If three parts have to be equal the total sum should be divisible by 3. If not we return false
# otherwise we start searching for target and if we find it three times in sequence then that means
# that three parts are possible.


from collections import defaultdict
from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total%3!=0:
            return False
        target = total//3
        original = target
        cnt = 0
        curr_sum=0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == target:
                cnt+=1
                if cnt==3:
                    return True
                target += original

        return False 
        
        '''
        cnt = 0
        d = {}
        curr_sum = 0
        prefix = []
        for i in range(len(arr)):
            curr_sum+=arr[i]
            if curr_sum not in d:
                d[curr_sum] = i 
        if curr_sum%3!=0:
            return False
        last = curr_sum
        target = last//3
        if target in d and last-target in d:
            i = d[target]
            j = d[last - target]
            if i < j < len(arr) - 1:
                return True
        
        return False     
        '''    