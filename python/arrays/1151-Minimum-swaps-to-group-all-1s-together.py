# Problem: Leetcode 1151 - Minimum Swaps to Group All 1's Together
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/
# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(n) - for the prefix sum array
# Approach: Use a sliding window of size equal to the number of 1's in the array. 
# For each window, count the number of 0's - which is done in O(1) due to prefix sum.(which represents swaps needed). Return the minimum swaps across all windows.


from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        prefix = [0]*(len(data)+1)
        zeros = 0
        swaps = float('inf')
        for i in range(len(data)):
            if data[i]==0:
                zeros+=1
            prefix[i+1] = zeros

        for i in range(0,len(data)-window+1):
            swaps=min(swaps,prefix[i+window]-prefix[i])
        return swaps