# Problem: Leetcode 2520 - Count the digits that divide a number
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: simply iterate over digits and count if they divide num

class Solution:
    def countDigits(self, num: int) -> int:
        cnt=0
        for digit in str(num):
            if num%int(digit)==0:
                cnt+=1
        return cnt