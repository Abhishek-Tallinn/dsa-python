# Problem: Leetcode 3614 - Process String with Special Operations II
# Difficulty: Hard
# Link: https://leetcode.com/problems/process-string-with-special-operations-ii/description/
# Time Complexity: O(n) as we loop through the string twice so O(n) + O(n) is O(n)
# Space Complexity: O(1) as we only use the length pointer
# Approach: Since res is too big to store in memory, we just loop through string and calculate the length of the final string.
# Then we iterate backwards and modify the length based on the character seen. Main issue is to deal with # character in backward iteration
# If # is found we check if k is in the second half of string i.e k+1>len//2 then k is reduced by len//2 and the len is updated by doing len-=len//2
# if char is % then k must be the mirror image so k is changed by length - k - 1
# if is a usual lowercase character then string must have increased by 1 so we just decrement length by 1. But before that
# we check is at the usual character k+1 == length(as string is 0 indexed) and if yes then it means were were looking for this particular character so we return it

class Solution:
    def processStr(self, s: str, k: int) -> str:
        #since there is exponentaial growth i cannot build res
        length = 0
        for char in s:
            if char == '%':
                pass
            elif char=='#':
                length*=2
            elif char=='*':
                if length:
                    length-=1
            else:
                length+=1
        if k+1 > length:
            return "."
        for c in reversed(s):
            if c=='*':
                length+=1
            elif c=='#':
                if k + 1 > (length)//2:
                    k-=length//2
                length = (length)//2
            elif c=='%':
                k = length - k - 1
            else:
                if k+1==length:
                    return c
                length-=1
        return "."
        