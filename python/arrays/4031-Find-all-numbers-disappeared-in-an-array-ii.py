# Problem: Leetcode 4031 - Find all numbers disappeared in an array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/Find-all-numbers-disappeared-in-an-array-II/description
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We loop over numbers and we take the missing numbers. then we loop over the missing number
# and everytime a gap is found we append an interval to the ans variable.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans = []
        missing = []
        s = set(nums)
        for i in range(lower,upper+1):
            if i not in s:
                missing.append(i)
                
        if not missing:
            return []
        left = 0
        for right in range(1,len(missing)):
            if missing[right] - missing[right-1]>1:
                ans.append([missing[left],missing[right-1]])
                left = right
        ans.append([missing[left],missing[-1]])
        return ans
        '''
        #solution without constucting any list

        
        nums = sorted(set(nums))   # deduplicate and sort
        ans = []
        prev = lower - 1           # track where we left off
        
        for num in nums:
            if num > upper:
                break
            if num < lower:
                continue
            if num > prev + 1:
                ans.append([prev + 1, num - 1])  # gap found
            prev = num
        
        # check gap after last num up to upper
        if prev < upper:
            ans.append([prev + 1, upper])
        
        return ans
        '''