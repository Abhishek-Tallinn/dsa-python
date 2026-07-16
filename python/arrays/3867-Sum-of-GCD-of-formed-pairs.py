# Problem: Leetcode 3867 - Sum of gcd of formed pairs
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/description/
# Time Complexity: O(n log n + n log max(val) as we iterate and calculate prefix GCD and n log n from sorting
# Space Complexity: O(n) as we make elements array and idx_list array
# Approach: We create prefix GCD as required and sort it then add nums in pairs by iterating till len(prefixGCD//2)
# We moved from using recursive GCD to python in built GCD for quick calculation

import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        #def gcd(a,b):
        #    if b==0:
        #        return a
        #    return gcd(b,a%b)
        prefixGCD = []
        mx = 0
        for num in nums:
            mx = max(mx,num)
            prefixGCD.append(math.gcd(num,mx))
        prefixGCD.sort()
        sumGCD = 0
        n = len(prefixGCD)
        for i in range(n//2):
            sumGCD += math.gcd(prefixGCD[i],prefixGCD[n-i-1])
        return sumGCD