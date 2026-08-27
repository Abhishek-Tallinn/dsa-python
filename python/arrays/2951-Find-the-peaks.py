# Problem: Leetcode 2951 - Find the peaks
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-peaks/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Excluding the first and last element we run a loop and check if any index is a mountain index
# and if yes we append the index to ans. at the end of the loop we return ans


from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(1,len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                ans.append(i)
        return ans