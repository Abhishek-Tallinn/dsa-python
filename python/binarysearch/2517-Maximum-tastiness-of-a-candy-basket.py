# Problem: Leetcode 2517 - Maximum tastiness of a candy basket
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-tastiness-of-a-candy-basket/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We convert the question to binary search on solution space. we sort the price array and then we say that
# the max diff that will allow us to select a basket of k things from the price array is between 0 and the difference between first and last array.
# based on this idea we return a binary search on solution space and keep recording the first true value of mid which is feasible.
# at the end we return this feasible amount. 
# appraoch2: we can also do the inverted template where we record the first infeasible solution and then return solution - 1 if its greater than 0 or we return 0
from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if len(set(price))<k:
            return 0
        mx=0
        mn = float('inf')
        price.sort()
        if k == 2:
            return price[-1]-price[0]
        def feasible(min_diff):
            count = 1
            last_selected = price[0]
            for i in range(1,len(price)):
                if price[i] - last_selected>=min_diff:
                    last_selected = price[i]
                    count+=1
            # Return True when infeasible (cannot select k candies)
            #return count < k
            #return true when feasible
            return count>=k

        left = 0 
        right = price[-1] - price[0]
        first_true_index = -1
        while left <= right:
            mid = (left+right)//2 
            if feasible(mid):
                first_true_index = mid
                #right = mid-1
                left = mid+1
            else:
                #left=mid+1
                right = mid-1
        return first_true_index
        #return first_true_index -1 if first_true_index>0 else 0