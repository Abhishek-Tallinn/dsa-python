# Problem: Leetcode 3248 - Snake in matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/snake-in-matrix/description/
# Time Complexity: O(m) where m is the number of commands
# Space Complexity: O(1)
# Approach: We simply change the x and y axis values based on command and finally return the index of the cell by the 
# given formula os (row*cols + col)

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = y = 0
        for command in commands:
            if command=="LEFT":
                x-=1
            elif command=="RIGHT":
                x+=1
            elif command=="UP":
                y-=1
            elif command=="DOWN":
                y+=1
        return y*n + x