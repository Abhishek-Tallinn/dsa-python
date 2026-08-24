# Problem: Leetcode 2544 - Alternating digit sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/alternating-digit-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We iterate and add the alternating digits to the total

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        for i,digit in enumerate(str(n)):
            if i%2==0:
                total+=int(digit)
            else:
                total-=int(digit)
        return total
