# Problem: Leetcode 901 - Online stock span
# Difficulty: Medium
# Link: https://leetcode.com/problems/online-stock-span/description/
# Time Complexity: O(1) as we only append and pop to stack
# Space Complexity: O(n) as we have to use a stack
# Approach: We add each prices to prices list and keep a track of indices in the stack list with help of idx.
# Then for each element we pop the stack indices till the prices of those indices ie less than or equal to the current price.
# THen we calculate the span once we have the top index.

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        self.idx = 0
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        if self.stack:
            span =  self.idx - self.stack[-1] 
        else:
            span = self.idx - 0 + 1
        self.stack.append(self.idx)
        self.idx+=1
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)