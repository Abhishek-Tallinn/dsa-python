# Problem: Leetcode 3751 - Total Waviness of Numbers in Range
# Difficulty: Medium
# Link: https://leetcode.com/problems/total-waviness-of-numbers-in-range/description/
# Time Complexity: O(n * log10(num2)). n is numbers while d is the total number of digits.
# Space Complexity: O(D) which is total number of digits as we turn the number into a string
# Approach: I have listed out two appraoches. 



class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        waviness = 0
        for num in range(num1,num2+1):
            if len(str(num))<3:
                continue
            elif num<1000:
                s = str(num)
                if int(s[1]) > int(s[0]) and int(s[1])>int(s[2])\
                or (int(s[1])<int(s[0]) and int(s[1])<int(s[2])):
                    waviness+=1
            else:
                s = str(num)
                for i in range(1,len(s)-1):
                    if (int(s[i])>int(s[i-1]) and int(s[i])>int(s[i+1])) \
                    or (int(s[i])<int(s[i-1]) and int(s[i]) < int(s[i+1])):
                        waviness+=1
        return waviness
            