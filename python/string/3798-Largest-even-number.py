# Problem: Leetcode 3798 - Largest even number
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-even-number/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: We iterate backward to find the first even digit at which point we break as that number would ofcourse be the largest.
# we keep track of the index just before the even digit and return string slice upto that index.
# if no even digit found then loop never break and index becomes 0 and empty string is returned which is what we want


class Solution:
    def largestEven(self, s: str) -> str:
        index = len(s)
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2==0:
                break
            index = i
        return s[:index]