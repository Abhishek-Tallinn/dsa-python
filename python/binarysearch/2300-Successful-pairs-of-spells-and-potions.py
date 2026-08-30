# Problem: Leetcode 2300 - Successful pairs of spells and potions
# Difficulty: Easy
# Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We convert the question to binary search on solution space. we sort the price array and then we say that
# the max diff that will allow us to select a basket of k things from the price array is between 0 and the difference between first and last array.
# based on this idea we return a binary search on solution space and keep recording the first true value of mid which is feasible.
# at the end we return this feasible amount. 
# appraoch2: we can also do the inverted template where we record the

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = [0]*len(spells)
        for j,spell in enumerate(spells):
            cnt = 0
            if spell*potions[-1] < success:
                continue
            left = 0
            right = m-1
            while left<=right:
                mid = (left+right)//2
                if spell*potions[mid] < success:
                    left = mid+1
                elif spell*potions[mid] >= success:
                    right = mid-1
            ans[j] = m-left
            
        return ans