# Problem: Leetcode 1502 - Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(1) if we don't count the space used by the sorting algorithm although timsort uses some space internally in python.
# Approach: Sort the array and check if the difference between consecutive elements is constant.
# Approach2: We can also use a mathematical approach where we find the minimum and maximum element and then check if the common difference is an integer and then check if all the elements in the progression are present in the array using a set. 
# this reduces time complexity to O(n) but space complexity will be O(n) due to the set data structure.
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i]!=d:
                return False
        return True
    
        '''    
        O(n) approach for mathematical solution:
        mn = min(arr)
        mx = max(arr)
        n = len(arr)

        if (mx - mn) % (n - 1) != 0:
            return False

        d = (mx - mn) // (n - 1)

        if d == 0:
            return len(set(arr)) == 1

        s = set(arr)

        for k in range(n):
            if mn + k*d not in s:
                return False

        return True
        '''