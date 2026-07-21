# Problem: Leetcode 551 - Student attendance record I
# Difficulty: Easy
# Link: https://leetcode.com/problems/student-attendance-record-i/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(1) as we use pointers
# Approach: We iterate over the string and keep check of Absent where we increment absent count.
# anytime the absent count goes over 1 we return False. Then we we find late we increment late count and check if it has reached 3 or more and if yes
# we then return false too. To calculate consecutive late count we keep resetting it everytime any character apart from L is encountered.

class Solution:
    def checkRecord(self, s: str) -> bool:
        cons_late = absent = 0
        for char in s:
            if char == 'L':
                cons_late+=1
                if cons_late >= 3:
                    return False
            elif char == 'A':
                absent += 1
                cons_late = 0
                if absent>1:
                    return False
            else:
                cons_late = 0
            
        return True