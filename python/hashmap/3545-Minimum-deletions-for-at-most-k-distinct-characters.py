# Problem: Leetcode 3545 - Minimum deletions for at most k distinct characters
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/
# Time Complexity: O(k log k) as we sort the dictionary to get the smallest values first.
# Space Complexity: O(n) as we use the dictionary data structures
# Approach: We calculate how many characters need to be deleted by doing len(d) - k. Then we need to delete these many character but since we want to acheive minimum we want to delete
# the character who have the least freq count. hence we sort our dictionary as per values and then we take list of the values and take that many lowest values for how many characters 
# need to be deleted. and then we return our answer

from collections import Counter
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d = Counter(s)
        to_delete = len(d)-k
        if to_delete<=0:
            return 0
        d = dict(sorted(d.items(), key=lambda x:x[1]))
        ans = 0
        l = list(d.values())
        for i in range(to_delete):
            ans+=l[i]
        return ans