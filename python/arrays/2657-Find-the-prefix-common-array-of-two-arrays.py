# Problem: Leetcode 2657 - Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
# Time Complexity: O(n) - as we go all elements of one permutation.
# Space Complexity: O(n) - as we use sets to store the seen elements of both arrays.
# Approach: Since current index is considered, we first element at the index into each set of A and B. then if the elements are equal we increment common count by 1. 
# If they are not equal then we check if the element of A is in seen_B and element of B is in seen_A then we increment common count by 2 as both elements are common.
# else if only element of one is seen in the other set but not both then again common_count goes up by 1 and we write the common count to the prefix common array.

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()
        common_count = 0
        pca = [-1]*len(A)
        for i in range(len(A)):
            seen_A.add(A[i])
            seen_B.add(B[i])
            if A[i]==B[i]:
                common_count+=1
            elif B[i] in seen_A and A[i] in seen_B:
                common_count+=2
            elif B[i] in seen_A or A[i] in seen_B:
                common_count+=1
            pca[i] = common_count
        return pca