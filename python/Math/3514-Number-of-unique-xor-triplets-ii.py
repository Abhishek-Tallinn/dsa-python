# Problem: Leetcode 3514 - Number of unique XOR triplets II
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description/
# Time Complexity: O(n^2+mn)
# Space Complexity: O(m)
# Approach: Its a math problem but unlike the xor triplet 1 there is no pattern here so we find the greatest power of 2 
# and make a boolean array of that length as no xor value will be greater than this. 
# then we intelligently find all possible xor of two elements first and record it in our boolean array
# then we may a second t boolean array and this time all values in the range of u if s[x] is false then we continue
# but if s[x] is true meaning that number was seen in array with run an inner loop and find its xor with each element in nums
# and record it in t as True for those indices. Only the true found in t matter and not s as s boolean array was only intermediate calculation. 
# then we return the number of true elements in t

from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = max(nums)
        u = 1
        while u <= mx:
            u<<=1
        s = [False] * u
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                s[nums[i]^nums[j]] = True
        t = [False] * u
        for x in range(u):
            if not s[x]:
                continue
            for v in nums:
                t[x^v] = True
        #return sum(1 for b in t if b)
        cnt = 0
        for val in t:
            if val:
                cnt+=1
        return cnt