# Problem: Leetcode 2363 - Merge similar items
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-similar-items/description/
# Time Complexity: O(n log n) as we sort the cost array in reverse
# Space Complexity: O(1) as we just use two pointers
# Approach: We use the traditional two pointer based merge technique combined with sentinal values 
# to merge and to avoid extra loops for the longer array
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort(key = lambda x:x[0])
        items2.sort(key=lambda x:x[0])
        ans = []
        #this is merge join SQL case
        i = j = 0
        while i<len(items1) or j<len(items2):
            v1 = items1[i][0] if i<len(items1) else float('inf')
            v2 = items2[j][0] if j<len(items2) else float('inf')
            if v1==v2:
                ans.append([v1, items1[i][1] + items2[j][1]])
                i+=1
                j+=1
            elif v1 < v2:
                ans.append(items1[i])
                i+=1
            else:
                ans.append(items2[j])
                j+=1

        return ans