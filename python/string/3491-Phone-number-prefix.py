# Problem: Leetcode 3491 - Phone number prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/phone-number-prefix/description/
# Time Complexity: O(n^2) since we use nested loops
# Space Complexity: O(1)
# Approach: Based on time input size we can have a nested loop and also a phone number could be prefixed to any other possibly in the list
# So its sensible to run a nested loop and check if one number is prefixed to any other number.

from typing import List

class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if j==i:
                    continue
                if numbers[j][:len(numbers[i])] == numbers[i]:
                    return False
        return True