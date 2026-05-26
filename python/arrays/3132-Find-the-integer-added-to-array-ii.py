# Problem: Leetcode 3132 - Find the Integer Added to Array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-integer-added-to-array-ii/description/
# Time Complexity: O(n log n) where n is the number of elements in the arrays as we have to sort
# Space Complexity: O(1) as no extra space used
# Approach: Main idea is that since two elements are removed then after sorting nums2[0] must match one of the first three elements of nums1.
# So we take all possible value of x and then for each value use two pointers to check if this value is valid. We start comparing each value of nums1 and nums2
# If they are equal both pointers move and if they are not then only pointer of nums1 move. We keep track of mismatches when only pointer of nums1 moves and if they are more than 2 then we break
# We add valid values of x to an array and return the min possible value

from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        possible_x = [nums2[0]-nums1[0], nums2[0]-nums1[1], nums2[0]-nums1[2]]
        valid_x = []
        for x in possible_x: # take each candidate value
            i,j=0,0
            mis = 0
            possible = True
            while i < len(nums1) and j < len(nums2):
                if nums1[i] + x == nums2[j]:
                    i+=1
                    j+=1
                else:
                    mis+=1
                    i+=1 #skip the element of nums1
                    if mis>2:
                        possible = False
                        break
            if possible:
                valid_x.append(x)

        return min(valid_x)