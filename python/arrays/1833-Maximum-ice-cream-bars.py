# Problem: Leetcode 1833 - Maximum ice cream bars
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-ice-cream-bars/description/
# Time Complexity: O(n log n) where n is the length of the array as we sort
# Space Complexity: O(n) as we sort counting and return a new array
# Approach: We are supossed to use counting sort to sort the array which we do. once sorted there is no better way that to buy
# ice creams from cheapest to costliest till we cannot buy any more 


from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def counting_sort(arr):
            mx = max(arr)
            count = [0]* (mx + 1)
            for num in arr:
                count[num]+=1
            res = []
            for value,freq in enumerate(count):
                res.extend([value]*freq)
            return res
        costs = counting_sort(costs)
        cnt = 0
        total = 0
        for cost in costs:
            if total+cost>coins:
                return cnt
            total+=cost
            cnt+=1
        return cnt

        