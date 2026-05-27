# Problem: Leetcode 541 - Reverse String II
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-string-ii/description/
# Time Complexity: O(n) - passing over each character of string
# Space Complexity: O(n) as we make a list and join it back
# Approach: We iterate in chunks of 2k and slice the reverse the first k elements on list of the original string.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        r_s = []
        left = 0
        jump = 2*k
        while left < len(s):
            curr_window = s[left:left+jump]
            temp = curr_window[0:k][::-1]+curr_window[k:]
            r_s.extend(temp)
            left+=jump
        return ''.join(r_s)