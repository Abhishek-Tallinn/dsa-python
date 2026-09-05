# Problem: Leetcode 1015 - Smallest integer divisible by k
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-integer-divisible-by-k/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We can just keep growing n with modular arithmetic and check if n is divisble by k and everytime we add 1 to the length counter
# as based on our formula the length grows by 1 

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        length=1
        n=1
        while n%k != 0:
            n=((n*10)%k+1)%k
            length+=1
        return length
        '''with remainder approach
        remainder = 1%k
        length = 1
        while remainder!=0:
            remainder = (remainder*10+1)%k
            length+=1
        return length
        '''
        '''OG solution
        def itos(n)->str:
            cnt=0
            while n>0:
                digit = n%10
                cnt+=1
                n//=10
            return cnt

        n = 1
        if k%2==0 or k%5==0:
            return -1
        while n%k != 0:
            n=n*10+1
        
        return itos(n)
        '''