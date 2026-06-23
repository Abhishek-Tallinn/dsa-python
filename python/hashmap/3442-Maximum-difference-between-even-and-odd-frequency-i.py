# Problem: Leetcode 3442 - Maximum difference between even and off frequency I
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-difference-between-even-and-off-frequencies/description/
# Time Complexity: O(n) we we go through the hashmap of the string
# Space Complexity: O(k) hashmap of k characters almost constant space
# Approach1: we simply make a hasmhmap of the string and we keep count of max off freq seen and minimum even freq seen and we return the difference.

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        mx_odd = 0
        mn_even = float('inf')
        for freq in freq.values():
            if freq%2==1:
                mx_odd = max(mx_odd,freq)
            else:
                mn_even = min(mn_even,freq)
        return (mx_odd - mn_even)