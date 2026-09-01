# Problem: Leetcode 2300 - Successful pairs of spells and potions
# Difficulty: Easy
# Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# Time Complexity: O(n log n) as we do a binary search over the array
# Space Complexity: O(1) as no extra data structure is added
# Approach: We sort potions and do a binary search to find the first index from where spell*potion value >=success. 
# then we update the answer array with the remanining number of potions value by doing len(potions)-left as left pointer will find the first
# index from where the value of spell*potion[i] becomes > success and since the relationship is monotonic
# we can just do ans[j] = len(spotions) - left

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