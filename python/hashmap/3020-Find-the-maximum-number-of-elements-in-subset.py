# Problem: Leetcode 3020 - Find the maximum number of elements in subset
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description/
# Time Complexity: O(n) as we go through the hashmap
# Space Complexity: O(n) as we use the dictionary 
# Approach: We make a hashamp as we need the frequencies and if we see 1 then we take the maximum length of subset we can make with 1. 
# If we see any number which has value>=2 meaning that we can possibly have a subset of the type that we need with this number,
# we simply find how many power os 2 of this number exists in the hasmap keeping a count. then we increment the maximum subset length by taking the 
# max of (mx,2*cnt+1) as 2*cnt will be the number of elements we can append in subset and +1 is for the starting number


from collections import Counter
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mx = 0
        d = Counter(nums)
        for key,value in d.items():
            if key==1:
                if value%2==0:
                    mx = max(mx,value-1)
                else:
                    mx=max(mx,value)
            elif value==1:
                continue
            elif value>=2:
                power = 2
                cnt = 0
                while key**power in d:
                    cnt+=1
                    if d[key**power]==1:
                        break
                    power*=2
                mx = max(mx, 2*cnt+1)
                
        return max(1,mx)