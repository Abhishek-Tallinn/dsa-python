# Problem: Leetcode 1064 - Fixed point
# Difficulty: Medium
# Link: https://leetcode.com/problems/fixed-point/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We do a binary search and find the mid which has arr[mid] == mid. then we also take our ans in answer variable
# and continue our search as we have to find the smallest index. finally we return ans


from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        ans = -1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == mid:
                ans = mid
                right = mid-1
            elif arr[mid]>mid:
                right = mid-1
            else:
                left = mid+1
        return ans
        '''
        O(n)
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1
        '''