# Problem: Leetcode 2917 - Find the k-or of an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/Find-the-k-or-of-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We find max number of bits by taking binary representation of the largest number in the array.
# then for each bit in that range we produce a mask and compare each number with that mask. If mask&num is true then we increment count
# if count for a bit is >=k then that means that this bit will be set in final answer which we do. 
# then we return the integer value of the final answer

from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        mx_bits = len(bin(max(nums))[2:])
        ans = ['0']*mx_bits
        for bit in range(0,mx_bits):
            mask = 1<<bit
            cnt = 0
            for num in nums:
                if num&mask:
                    cnt+=1
            if cnt>=k:
                ans[mx_bits - bit - 1] = '1'
        return int(''.join(ans),2)