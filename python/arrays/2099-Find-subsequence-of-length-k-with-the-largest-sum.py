# Problem: Leetcode 2099 - Find subsequence of length k with the largest sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Input size allows us to take the index of both elements direcltly in O(n) and all elements being distinct
# also helps. Then we can check if to remove both elements from one side or both from the other side 
# or to remove one element from each side 

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        ans = []
        index_map = {}
        for idx,num in enumerate(nums):
            if num in index_map:
                index_map[num].append(idx)
                continue
            index_map[num] = [idx]
        temp = sorted(nums)[-k:]
        indices = []
        for num in temp:
            indices.append(index_map[num].pop())
        indices.sort()
        for i in indices:
            ans.append(nums[i])
        return ans
        '''
        indices_of_k_largest = sorted(range(len(nums)), key=lambda i: nums[i])[-k:]
      
        return [nums[i] for i in sorted(indices_of_k_largest)]
        '''