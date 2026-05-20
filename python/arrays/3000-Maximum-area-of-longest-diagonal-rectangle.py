# Problem: Leetcode 3000 - Maximum Area of Longest Diagonal Rectangle
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/
# Time Complexity: O(n) - as we go through the matrix once
# Space Complexity: O(1) as no additional data structure is used.
# Approach: We iterate through the elements and take length and width for each value. Then if the diagonal is greater than the max diagonal seen till now we update the max area ot the new area.
# If the diagonal is same as max diagonal then we take the max of the area and the max area seen till now. Finally we return the max area.

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for row in dimensions:
            l,w = row
            if l*l + w*w > max_diagonal:
                max_diagonal = l*l+w*w
                max_area = l*w
            elif l*l+w*w == max_diagonal:
                max_area = max(max_area, l*w)
        

        return max_area