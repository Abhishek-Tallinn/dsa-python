# Problem: Leetcode 3300 - Minimum element after replacement with digit sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
# Time Complexity: O(n.k) where k is the length of each number but reduces to O(n)
# Space Complexity: O(1) as no extra space used
# Approach: We simply loop over the array and add the calculate sum of digits and keep a min ans variable which we keep updating 



from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        mn = float('inf')
        for num in nums:
            s = sum(int(d) for d in str(num))
            mn = min(mn,s)

        return mn