# Problem: Leetcode 922 - Sort array by parity II
# Difficulty: Easy
# Link: https://leetcode.com/problems/sort-array-by-parity-ii/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: we extract even and odds and then we append them in ans array depending on if the index is even or odd.
# appraoch2: can we do it in place???

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = [i for i in nums if i%2==1]
        evens = [i for i in nums if i%2==0]
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                ans.append(evens.pop())
            else:
                ans.append(odds.pop())
        return ans   