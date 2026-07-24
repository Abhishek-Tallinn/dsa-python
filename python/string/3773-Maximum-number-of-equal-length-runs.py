# Problem: Leetcode 3773 - Maximum number of equal length runs
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-number-of-equal-length-runs/description/
# Time Complexity: O(n) as we loop once 
# Space Complexity: O(n) as we use a hashmap
# Approach: We keep a count of the length of each 'run' found in the string in the hashmap with the length of the run being 
# our key in the hasmap and we increment its count everytime a run of that length is found.
# then we return the maximum of these values

from collections import defaultdict
class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        d = defaultdict(int)
        i = 0
        mx_len = 0
        while i < len(s):
            j = i
            while j+1<len(s) and s[j] == s[j+1]:
                j+=1

            d[(j-i+1)] += 1
            i=j+1

        return max(d.values())
        