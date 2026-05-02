# Problem: Leetcode 788 - Rotated Digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotated-digits/description/
# Time Complexity: O(n * d). n is numbers while d is the total number of digits.
# Space Complexity: O(log n + m) where m is the total digits across the number and log n for the string conversion.
# Approach: I have listed out two appraoches. 
# Approach 1- brute forces but coverting every valid number to its mirror version and comparing with the original and accordingly incrementing count
# Approach 2- we can also just check if the number contains any of the valid digits and any of the mirrorable digits. If it contains any of the mirrorable digits, we can increment the count as we know that it will be a good number. This seems to be more pythonic

class Solution:
    def rotatedDigits(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 1
        count = 0
       
        for i in range(1,n+1):
            if i in {0,1,3,4,7,8}:
                continue
            #else rotate and check
            rotated_num = []
            isGood = True
            for digit in str(i):
                if digit in {"3","4","7"}: #set for O(1) look up
                    isGood = False
                    break
                elif digit in {"0","1","8"}:
                    rotated_num.append(digit)
                elif digit=="2":
                    rotated_num.append("5")
                elif digit=="5":
                    rotated_num.append("2")
                elif digit=="6":
                    rotated_num.append("9")
                elif digit=="9":
                    rotated_num.append("6")
            if not isGood:
                continue
            final_rotated_num = int(''.join(rotated_num))
            if final_rotated_num!=i:
                count+=1
        return count
        '''
        valid = {'0','1','2','5','6','8','9'}
        can_mirror = {'2','5','6','9'}
        for i in range(1,n+1):
            digits = str(i)
        
            if any(d not in valid for d in digits):
                continue
            if any(d in can_mirror for d in digits):
                count+=1
        return count
        '''