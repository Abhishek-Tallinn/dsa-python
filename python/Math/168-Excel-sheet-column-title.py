# Problem: Leetcode 168 - Excel sheet column title
# Difficulty: Easy
# Link: https://leetcode.com/problems/excel-sheet-column-title/description/
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: The key insight is that alphabets start from 1 and not 0 so according to base 26 system then is a 1 added to every alphabet.
# Now we simple calculate the modulus remainder and add ord('A') to it to get our alphabet and then reduce column number by //26. but the gotcha moment 
# is that we have to subtract 1 on each iteration to convert it to base 26 otherwise the answer is wrong

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        title = []
        while columnNumber > 0:
            columnNumber-=1
            title.append(chr(columnNumber %26 + 65))
            columnNumber = columnNumber//26
        return ''.join(title[::-1])