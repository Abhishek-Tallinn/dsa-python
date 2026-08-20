# Problem: Leetcode 3072 - Distribute elements into two arrays II
# Difficulty: Hard
# Link: https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/description/
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Approach: Since input size is 10^5 we need to do it in O(n log n) time and hence we use the array copies maintaining sorted lists
# and then we insert each value with bisect_right and then return the current length of that array minus the index with bisect right to know the 
# current amount of elements greater than that value. This way solution is O(n log n)

from sortedcontainers import SortedList
from bisect import bisect_right
from typing import List
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def greaterCount(arr,val):
            idx = arr.bisect_right(val)
            return len(arr)-idx
            
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        arr1copy = SortedList(arr1)
        arr2copy = SortedList(arr2)
        l1 = l2=1
        for i in range(2,len(nums)):
            if greaterCount(arr1copy,nums[i]) > greaterCount(arr2copy,nums[i]):
                arr1.append(nums[i])
                arr1copy.add(nums[i])
                l1+=1
            elif greaterCount(arr1copy,nums[i]) < greaterCount(arr2copy,nums[i]):
                arr2.append(nums[i])
                arr2copy.add(nums[i])
                l2+=1
            else:
                if l1>l2:
                    arr2.append(nums[i])
                    arr2copy.add(nums[i])
                    l2+=1
                elif l1<=l2:
                    arr1.append(nums[i])
                    arr1copy.add(nums[i])
                    l1+=1
            
        return arr1+arr2