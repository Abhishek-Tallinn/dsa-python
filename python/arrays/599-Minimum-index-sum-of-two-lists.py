# Problem: Leetcode 599 - Minimum index sum of two lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
# Time Complexity: O(n^2) as we use nested loop to find common elements
# Space Complexity: O(n) as we make common and ans array
# Approach: We make a nested loop pass over the two lists and we keep track of the least common index sum while also
# picking up the common string with their index sum. Then we iterate over the common strings found and if their index sum is 
# equal to the least index sum we found in first nested iteration then we take them together.

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_idx_sum = float('inf')
        common = []
        for i,s1 in enumerate(list1):
            for j,s2 in enumerate(list2):
                if s1==s2:
                    least_idx_sum = min(least_idx_sum,i+j)
                    common.append((i+j,s1))
                    break
        ans = []
        for idx_sum, s in common:
            if idx_sum == least_idx_sum:
                ans.append(s)
        return ans