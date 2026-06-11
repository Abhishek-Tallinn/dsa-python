# Problem: Leetcode 251 - Flatten a 2D Vector
# Difficulty: Medium
# Link: https://leetcode.com/problems/flatten-a-2d-vector/description/
# Time Complexity: O(1) for next() and hasNext()
# Space Complexity: O(m*n) where m is the number of rows and n is the average number of elements per row
# Approach: We flatten the 2D vector into a 1D list during initialization and use an index to keep track of the next element to find 
# and we keep moving that index. If index reached the last element then hasNext will return false as there are no more elements.

from typing import List

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vector = vec
        self.flat_vector = [e for row in self.vector for e in row]
        self.i = -1
        

    def next(self) -> int:
        self.i+=1
        return self.flat_vector[self.i]

    def hasNext(self) -> bool:
        return self.i < (len(self.flat_vector) - 1)