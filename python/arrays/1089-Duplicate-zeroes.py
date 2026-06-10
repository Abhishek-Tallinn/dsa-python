# Problem: Leetcode 1089 - Duplicate Zeros
# Difficulty: Easy
# Link: https://leetcode.com/problems/duplicate-zeros/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: First pass to count zeros and determine the final length of how many element from original array will fit into the new array. Second pass to fill the array from the end.
# we need to handle the special case if the last element we count was a zero. If it is we write a zero in the last place and decrement the write pointer and source_index both.

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        source_index = -1
        dest_index = 0
        while dest_index < len(arr):
            source_index+=1
            if arr[source_index] == 0:
                dest_index+=2
            else:
                dest_index+=1
        write_pos = len(arr)-1
        #handle special case
        if dest_index == len(arr)+1:
            arr[write_pos] = 0
            source_index-=1
            write_pos-=1
        #loop back
        while write_pos>0:
            if arr[source_index] == 0:
                arr[write_pos] = 0
                arr[write_pos-1]=0
                write_pos-=1
            else:
                arr[write_pos] = arr[source_index]
            source_index-=1
            write_pos-=1
