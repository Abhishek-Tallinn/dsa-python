# Problem: Leetcode 2678 - Number of senior citizens
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-senior-citizens/description/
# Time Complexity: O(n) - as we go over the scores in the array.
# Space Complexity: O(1)
# Approach: We iterate and take the age (slice from 11 to 13) for each details and check if its > 60 and increment cnt and then return cnt

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for detail in details:
            age = detail[11:13]
            if int(age)>60:
                cnt+=1
        return cnt