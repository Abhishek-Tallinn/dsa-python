# Problem: Leetcode 2452 - Words withing two edits of dictionary
# Difficulty: Medium
# Link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/
# Time Complexity: O(n +m) worse case as the two pointers can traverse full array and not find a match.
# Space Complexity: O(1) as we only use two pointers
# Approach1: We run two pointers separately on nums1 and nums2 utilizing the fact that the arrays are sorted. Only the pointer
# which is at a lower value than the other pointer gets incremented to check equality. If common value not found we return -1.
# Approach2: We can just convert nums2 to a set and iterate over the values of nums1 and checks its existence in nums2 and return the first value that we find. 
# This approach use O(n+m) time complexity and O(m) space as we make a set. So space complexity is higher


from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #two pointers as array sorted
        i=j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1

        #direct set approach
        '''
        nums2=set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                return nums1[i]
        return -1
        '''