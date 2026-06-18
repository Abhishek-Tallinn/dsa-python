# Problem: Leetcode 771 - Jewels and Stones
# Difficulty: Easy
# Link: https://leetcode.com/problems/jewels-and-stones/description/
# Time Complexity: O(n) as we iterate over stones. set look up is O(1)
# Space Complexity: O(n) as we makes jewels into a set
# Approach: jewels are converted to set for fast look up. Then we iterate over stones and look up if stone exists in jewels and add to cnt.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        cnt=0
        for stone in stones:
            if stone in jewels:
                cnt+=1
        return cnt