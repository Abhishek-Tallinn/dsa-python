# Problem: Leetcode 3819 - Rotate non negative elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-non-negative-elements/description/
# Time Complexity: O(n) - as we go through all the element of nums and then once over idx_list so O(n+m) which reduces to O(n)
# Space Complexity: O(n) as we make elements array and idx_list array
# Approach: Just filter the positive elements. we cannot rotate the positive elements by slicing due to time constraint. so we just loop through nums and if index is in idx_list we update the nums[i] 
# with rotated index in elements i.e (j+k)%len(elements). to check membership fast we need to convert idx_list to a set

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        
        idx_list = []
        elements = []
        for idx,num in enumerate(nums):
            if num>=0:
                idx_list.append(idx)
                elements.append(num)
        # now we have element list
        if not elements:
            return nums
        
        k=k%len(elements)
        #idx_set = set(idx_list)
        
        for j,idx in enumerate(idx_list):
            nums[idx] = elements[(j+k)%len(elements)]
        #for i in range(len(nums)):
        #    if i in idx_set:
        #        nums[i] = elements[(j+k)%len(elements)]
                
        #        j+=1
        return nums
        