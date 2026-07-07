# Problem: Leetcode 3756 - Concatenate Non-Zero Digits and Multiply by Sum II
# Difficulty: Medium
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description/
# Time Complexity: O(n) as we loop on many arrays but its O(n) as we loop separately
# Space Complexity: O(n) as we use digits and positions array to store the non-zero digits
# Approach: We use prefix sums to canculate the sum of digits which we can get in O(1) time due to pre computed prefix array of sum of digits of the string.
# Similarly we precompute the number possible based on the query range and we are have a powers array which we use to computer a substring of the whole string. Then with prefix nums
# We can precompute the number also in O(1) time. Then we multiply the two and return the answer.

from typing import List
import bisect
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MODULO = 10**9 + 7
        n = len(s)

        prefix_sum = [0] 

        digits = []
        positions = []
        for i in range(len(s)):
            prefix_sum.append(prefix_sum[-1]+int(s[i]))

        for i, ch in enumerate(s):
            d = int(ch)

            if d != 0:
                digits.append(d)
                positions.append(i)

        m = len(digits)
        prefix_num = [0] 

        for i in range(len(digits)):
            prefix_num.append((prefix_num[-1]*10+digits[i])%MODULO)

        pow10 = [1] * (m + 1)

        for i in range(1, m+1):
            pow10[i] = (pow10[i-1] * 10) % MODULO


        ans = []
        for start, end in queries:

            digit_sum = prefix_sum[end+1] - prefix_sum[start]

            left = bisect.bisect_left(positions, start)
            right = bisect.bisect_right(positions, end)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            num = (
                prefix_num[right]
                - prefix_num[left] * pow10[length]
            ) % MODULO

            ans.append((num * digit_sum) % MODULO)

        return ans