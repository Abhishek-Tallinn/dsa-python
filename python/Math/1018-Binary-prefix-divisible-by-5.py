# Problem: Leetcode 1018 - Binary prefix divisible by 5
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We can take the starting digit and its correspodning binary number in start and update answer array if start%5=0
# otherwise we loop and instead of calculating the new value from incoming binary digit, we just double start if a 0 comes in binary number
# and we do start*2+1 if an odd binary digit comes in. and each time we check if its divisible by 5 to update answer array
# we dont need to recalculate the new binary number each time when binary digit comes in.

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = [False]*len(nums)
        s=str(nums[0])
        start = int(s,2)
        if start%5==0:
            answer[0] = True
        for i in range(1,len(nums)):
            if nums[i]==0:
                start*=2
            else:
                start = start*2+1
            if start%5==0:
                answer[i]=True
        return answer