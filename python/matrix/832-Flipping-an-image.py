# Problem: Leetcode 832 - Flipping an Image
# Difficulty: Easy
# Link: https://leetcode.com/problems/flipping-an-image/description/
# Time Complexity: O(mxn) as we traverse the matrix to flip and invert it
# Space Complexity: O(1) as we are modifying the matrix in-place.
# Approach: We iterate the matrix and reverse each row in place with reverse method. We could also use the two pointer appraoach to reverse it.
# Then we traverse the matrix again and we flip each bit with XOR. We can also do this in one pass by traversing each row and flipping it while also inverting it at the same time.
# But this is cleaner.


from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] ^= 1
        return image
        