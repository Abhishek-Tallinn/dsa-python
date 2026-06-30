# Problem: Leetcode 1846 - Maximum element after decreasing and rearranging
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/
# Time Complexity: O(n log n) as we sort  
# Space Complexity: O(n) for approach 1 and O(1) for approach 2
# Approach1: We keep a result array and then after sorting the input array we iterate over it. Then first element of res is set to 1.
# then we see that if the element of input arr is <=1 from previous element in res(which can be reduced anyway) then we append this element to res.
# else we append res[i-1]+1 to res as we can reduce an arr element at any time. THen we just return res[-1] as the last element is guaranteed to be the smallest.
# Approach2: We just sort the array and keep going through the array to see if the current element is more than 1 distance away from the previous element.
# If it its then our ans is incremented by 1 as we can reduce a larger element to be the next higher number from the current number in the array. and if not,
# in which case it means that the arr[i] element is as as our current value of ans, we just keep moving without increment ans.
# then we just return ans

from typing import List
from collections import Counter

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = [1]
        ans = 0
        for i in range(1,len(arr)):
            if arr[i]-res[-1]<=1:
                res.append(arr[i])
            else:
                res.append(res[i-1]+1)
        return res[-1]
        '''
        arr.sort()
        ans = 1
        for i in range(1,len(arr)):
            if arr[i]>=ans+1:
                ans+=1
        return ans
        '''

        






        

        
        

        