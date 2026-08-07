# Problem: Leetcode 338 - Counting Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/counting-bits/description/
# Time Complexity: O(n log n) as we iterate through the numbers and for each number we calculate the number of 1s in its binary representation
# Space Complexity: O(1)
# Approach: We iterate through the numbers and calculate the number of 1s in its binary representation

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        def ones(i):
            cnt = 0
            while i > 0:
                if i%2==1:
                    cnt+=1
                i = i //2
            return cnt
        for i in range(n+1):
            ans[i] = ones(i)
        return ans