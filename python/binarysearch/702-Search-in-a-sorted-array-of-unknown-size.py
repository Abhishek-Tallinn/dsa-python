# Problem: Leetcode 702 - Search in a Sorted Array of Unknown Size
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
# Time Complexity: O(log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We first find array boundaries as we keep incrementing right till the value at right is less than target.
# we also keep track of previous right value in left to keep our binary search narrow. Then we run usual binary search



# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1
        while reader.get(right)<target:
            left = right #would narrow the binary search
            right<<=1
        while left<=right:
            mid = (left+right)//2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid+1
            else:
                right = mid-1
        return -1