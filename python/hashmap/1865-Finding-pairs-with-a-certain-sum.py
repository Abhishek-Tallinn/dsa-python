# Problem: Leetcode 1865 - Finding Pairs with a Certain Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/
# Time Complexity: O(n) as add operation would be in O(1) count would be O(n)
# Space Complexity: O(n) 
# Approach: We convert both lists to hashmaps and then on add operation either we change the value of hashmap key if it exists
# or we add the new kye to the hashmap. On the count operation we iterate on nums1 as its much smaller
# just like two sum we check if corresponding key which adds up to total exists in the largest nums2 hashmap. If it does
# then we multiply the values of both keys as that is the number of pairs that they will make. 

from collections import Counter
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.s1 = Counter(nums1)
        self.nums2 = nums2
        self.s2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        self.s2[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.s2[self.nums2[index]]+=1
        

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.s1:
            if (tot - num) in self.s2:
                cnt+= (self.s2[tot-num] * self.s1[num])

        return cnt
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)