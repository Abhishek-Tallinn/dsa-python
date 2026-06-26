# Problem: Leetcode 2864 - Maximum odd binary number
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-odd-binary-number/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make the answer array
# Approach: we iterate and count the number of 1s and 0s. if there is no zero we return s. if there is only one zero then we have to place it as LSB position to make an odd number and return it.
# Else we make our answer array first filled with 0s. we place a one at the LSB to make odd number and all other 1s are placed from the MSB positions for starting from first pos onwards.
# then we return our ans array after converting to a string

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = ones = 0
        for char in s:
            if char == '1':
                ones+=1
            else:
                zeros+=1
        if zeros==0:
            return s
        ans = ['0']*len(s)
        if ones == 1:
            ans[-1] = '1'
            return ''.join(ans)
        ans[-1]='1'
        ones-=1
        #ans[0:ones] = ['1'] * ones
        for i in range(ones):
            ans[i]='1'
        return ''.join(ans)