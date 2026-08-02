# Problem: Leetcode 36 - Valid Sudoku
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-sudoku/description/
# Time Complexity: O(n) except checking sub boxes which is O(n^2) as we have to iterate through all the sub boxes
# Space Complexity: O(1) - we have set but we only ever store 27 values in it
# Approach: We check each row and each column and then each sub box to check for repetition of the digits. if repetition found then we return False
# we can optimize by making a repetition function which can be reused.
# and sub box can be done with list comprehension


from rpds import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(board):
            for row in board:
                s = set()
                for e in row:
                    if e == ".":
                        continue
                    if e in s:
                        return False 
                    s.add(e)
            return True

        def checkColumns(board):
            for col in zip(*board):
                s = set()
                for e in col:
                    if e==".":
                        continue
                    if e in s:
                        return False
                    s.add(e)
            return True

        def checkSub(board):
            for i in range(0,len(board)-2,3):
                for j in range(0,len(board[0])-2,3):
                    s = set()
                    row1 = board[i][j:j+3]
                    row2 = board[i+1][j:j+3]
                    row3 = board[i+2][j:j+3]
                    full_square = row1+row2+row3
                    for val in full_square:
                        if val==".":
                            continue
                        if val in s:
                            return False
                        s.add(val)
            return True
                    
        return checkRows(board) and checkColumns(board) and checkSub(board)
