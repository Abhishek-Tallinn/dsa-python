# Problem: Leetcode 2553 - Separate the digits in an array
# Difficulty: Easy
# Link: https://leetcode.com/problems/separate-the-digits-in-an-array/description/
# Time Complexity: O(d) where d are the total digits to be processed
# Space Complexity: O(d) as digits have to stored in the return array
# Approach: This is a straighforward question where every number in nums is split for digits and the digits are stored and returned in the answer array.


from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            digit_array = [int(d) for d in str(num)]
            answer.extend(digit_array)

        return answer
        