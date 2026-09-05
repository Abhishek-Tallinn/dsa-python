# Problem: Leetcode 1056 - Confusing number
# Difficulty: Easy
# Link: https://leetcode.com/problems/confusing-number/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) as we store the reverse number
# Approach: If invalid digit found we immediately return False. Otherwise we keep appending the rotations or same digits as per rules
# at end end we rotate our reverse array and return the comparison that original n is not equal to the reverse joined integer

class Solution:
    def confusingNumber(self, n: int) -> bool:
        reverse = []
        og = n
        n = str(n)
        for i in range(len(n)):
            if n[i] in ('0','1','8'):
                reverse.append(n[i])
            elif n[i] == '6':
                reverse.append('9')
            elif n[i]=='9':
                reverse.append('6')
            else:
                return False
        if not reverse:
            return False
        reverse = reverse[::-1]
        return og != int(''.join(reverse))