from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []
        ans = []
        for i,num in enumerate(nums):
            if num == key:
                indices.append(i)
        for i in range(len(nums)):
            for idx in indices:
                if abs(i-idx) <= k:
                    ans.append(i)
                    break
        return sorted(ans)