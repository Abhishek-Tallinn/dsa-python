# Problem: Leetcode 1475 - Final prices with a special discount in a shop
# Difficulty: Medium
# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# Time Complexity: O(n) as we only append and pop to stack
# Space Complexity: O(n) as we have to use a stack
# Approach: We keep adding indices to stack and keep popping them if the value is greater than current element 
# to reach the closest element which has lower value than the current element and then we calculate the discount.

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #stack approach
        ans = prices[:]
        stack = []
        for i in range(len(prices)-1,-1,-1):
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            if stack:
                ans[i] = prices[i] - prices[stack[-1]]
            stack.append(i)
        return ans

        '''
        brute force
        answer = prices
        for i in range(len(prices)):
            
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    answer[i] = prices[i]-prices[j]
                    break
            
        return answer
        '''