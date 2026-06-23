# Problem: Leetcode 1189 - Maximum number of balloons
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-number-of-balloons/description/
# Time Complexity: O(n) - as we make a dictionary and pass over each key
# Space Complexity: O(1) as dict only have 5 characters
# Approach: Since we have to make a particular work balloon we identify the limiting factor which is the alphabet which has minimum availaibility to be used.
# for b,a,n it is their count and for l and o it is their count//2. so we loop through the hashmap and calculate the minimum value.

from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        valid = {'b','a','l','o','n'}
        d = defaultdict(int)
        for char in text:
            if char in valid:
                d[char]+=1
        if len(d)<5:
            return 0
        mn = float('inf')
        for char,value in d.items():
            if char == 'l' or char=='o':
                mn = min(mn,value//2)
            else:
                mn = min(mn,value)
        return mn
    

        
        