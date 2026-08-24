# Problem: Leetcode 2554 - Maximum number of integers to choose from a range I
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we have a set
# Approach: We run a loop on the range and we take those element that dont occur in banned and as long as current sum is within the total sum
# if total sum exceeds maxSum we break early

from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        total = 0
        cnt = 0
        for i in range(1,n+1):
            if i in b:
                continue
            if total+i>maxSum:
                break
            total+=i
            cnt+=1