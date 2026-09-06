# Problem: Leetcode 997 - Find the town judge
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-town-judge/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: We keep two arrays where people are represented by indices. We mark the trust received and also the trust given.
# then we loop over our trusted array and check if a person has received trust of n-1 people except themselves and also they have given trust to zero people
# in the other array then we immediately return their index as we have identified the town judge.

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        if not trust:
            return -1
        trusted = [0]*(n+1)
        trust_given = [0]*(n+1)
        for t in trust:
            p1,p2 = t
            trusted[p2]+=1
            trust_given[p1]+=1
        for i,trustLevel in enumerate(trusted):
            if trustLevel == n-1 and trust_given[i]==0:
                return i
        return -1