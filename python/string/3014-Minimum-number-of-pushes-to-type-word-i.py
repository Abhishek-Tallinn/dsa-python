# Problem: Leetcode 3014- Minimum number of pushes to type word I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-I/description/
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: Since we are allowed to rearrange letters any way that we want we will ofcourse arrange them 
# in the best possible places so we take the string and start keeping letter in all 1st positions and then all second positions on the number and so on.
# so total presses required will be basically dependent on the length of the string.


class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        print(n)
        if n<=8:
            return n
        elif n>8 and n<=16:
            return 8+2*(n-8)
        elif n>16 and n<=24:
            return 24+3*(n-16)
        else:
            return 48+ 4*(n-24)