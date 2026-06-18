# Problem: Leetcode 806 - Number of lines to write string
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-lines-to-write-string/description/
# Time Complexity: O(n) as we iterate over string
# Space Complexity: O(1)
# Approach: Straight forward idea that we iterate over string and keep a line width check and a line counter check. in the loop before incrementing line width
# we check if adding the current character would overflow the line. if yes then instead of increasing the line we increment the line counter and move to new line so 
# we set line width to 0. then new character is added to line width. the final line width would give us last line width

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line_width = 0
        line_counter=1
        for char in s:
            #if current line would overflow then just check first,
            # if yes then increase line counter and reset the line.
            # dont continue as we need to populate new line width
            if line_width+widths[ord(char)-ord('a')]>100:
                line_counter+=1
                line_width = 0
            line_width += widths[ord(char)-ord('a')]
            
        return [line_counter, line_width]