# Problem: Leetcode 3875 - Construct uniform parity array I
# Difficulty: Easy
# Link: https://leetcode.com/problems/construct-uniform-parity-array-i/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: If array is all odd or even then its already True. and if it has both odd and even elements
# then we can always take any even element and subtract any odd element from it and make it odd.
# so it will always be possible to sort the array to all odd elements in this case.

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True