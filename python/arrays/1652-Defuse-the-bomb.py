# Problem: Leetcode 1652 - Defuse the bomb
# Difficulty: Easy
# Link: https://leetcode.com/problems/defuse-the-bomb/description/
# Time Complexity: O(n) due to single pass through the array.
# Space Complexity: O(n) due to the result array.
# Approach: We triple the array to be able to check ahead and behind and this is possible due to small input size otherwise we can always use modulus
# to rotate the indices. based on value of K for each value of i we keep writing the same of k values ahead or behind the index into 
# the ans list which we return as an answer.

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = [0]*len(code)
        n = len(code)
        code = code+code+code
        for i in range(n,2*n,1):
            if k > 0:
                ans[i-n] = sum(code[i+1:i+1+k])
            if k == 0:
                ans[i-n] = 0
            if k < 0:
                ans[i-n] = sum(code[i-abs(k):i])
        return ans