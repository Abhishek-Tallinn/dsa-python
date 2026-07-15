# Problem: Leetcode 3658 - GCD of odd and even sums
# Difficulty: Easy
# Link: https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach1: We simply realize that difference between sums will be n and thats the GCD
# Appraoch2: we actually calculate the sums and then use recursive GCD function


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

        '''
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)

        sumOdd=sumEven = 0
        for i in range(1,2*n+1):
            if i%2==1:
                sumOdd+=i
            else:
                sumEven+=i
        
        return gcd(sumOdd,sumEven)
        '''