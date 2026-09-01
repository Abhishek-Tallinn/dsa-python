# Problem: Leetcode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/description/
# Time Complexity: O(n) - as we iterate through the string
# Space Complexity: O(1) - as we only use a constant amount of extra space(our model string idea is a lot of overhead)
# Approach: We take even or odd length strings separately and for even length we return half the minimum number of mismatches if we start from 0 or 1.
# for odd strings we have to make this choice that if ones > zeros then we only calculate start 1 mismatches and return mismatch//2
# and if zeros>ones we return mismatchs//2 for start 0 mismatches. If the difference between ones and zeros is greater than 1 we return -1 as it is impossible to make it alternating.
# because for odd length strings there is only one way to make them.
from typing import List

class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s)==1:
            return 0
        start_1 = start_0 = 0
        ones = s.count('1')
        zeros = len(s)-ones
        if len(s)%2==0:
            if ones!=zeros:
                return -1
            for i in range(len(s)):
                if i%2==0:
                    if s[i]=='0':
                        start_1+=1
                    elif s[i]=='1':
                        start_0+=1
                else:
                    if s[i]=='1':
                        start_1+=1
                    elif s[i]=='0':
                        start_0+=1
            return min(start_0//2,start_1//2)

        elif len(s)%2==1:
            if abs(ones-zeros)!=1:
                return -1
            if ones>zeros:
                for i in range(len(s)):
                    if i%2==0:
                        if s[i]=='0':
                            start_1+=1
                    else:
                        if s[i]=='1':
                            start_1+=1
                return start_1//2
            else:
                for i in range(len(s)):
                    if i%2==0:
                        if s[i]=='1':
                            start_0+=1
                    else:
                        if s[i]=='0':
                            start_0+=1
                return start_0//2
        '''
        OG solution
        ones = s.count('1')
        zeros = s.count('0')
        swaps = 0
        if len(s)%2==1:
            if ones > len(s)//2+1 or zeros > len(s)//2+1:
                return -1
            model_string = []
            if ones>zeros:
                for i in range(len(s)):
                    if i%2==0:
                        model_string.append('1')
                    else:
                        model_string.append('0')
            elif ones<zeros:
                for i in range(len(s)):
                    if i%2==0:
                        model_string.append('0')
                    else:
                        model_string.append('1')
            for i in range(len(s)):
                if s[i]!=model_string[i]:
                    swaps+=1
            return swaps//2

        elif len(s)%2==0:
            if ones > len(s)//2 or zeros > len(s)//2:
                return -1
            start0 = []
            start1 = []
            for i in range(len(s)):
                if i%2==0:
                    start0.append('0')
                    start1.append('1')
                else:
                    start0.append('1')
                    start1.append('0')
            diff1=diff2=0
            for i in range(len(s)):
                if s[i]!=start0[i]:
                    diff1+=1
                if s[i]!=start1[i]:
                    diff2+=1
            return min(diff1//2,diff2//2)
            '''