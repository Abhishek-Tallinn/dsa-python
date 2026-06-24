# Problem: Leetcode 3121 - Check if two chessboard squares have the same colour
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-colour/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: We directly check the parity of the squares given. if the parity of the squares which is (col_index+row_index)%2 equal then they will have the same colour.

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        c1 = (ord(coordinate1[0]) - ord('a') + int(coordinate1[1])) % 2
        c2 = (ord(coordinate2[0]) - ord('a') + int(coordinate2[1])) % 2

        return c1 == c2