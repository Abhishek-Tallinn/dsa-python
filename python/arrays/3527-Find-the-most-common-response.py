# Problem: Leetcode 3527 - Find the most common response
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-most-common-response/description/
# Time Complexity: O(n^2)
# Space Complexity: O(n) as we use dictionary and also convert back to the list
# Approach: We collect unique values in the 2D list and count freq with dicionary and extract the values with maximum frequence and then sort it
# then we return the very first element

from typing import List
from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        filtered_responses = []
        for i in responses:
            filtered_responses.append(list(set(i)))
        flat_response = [r for row in filtered_responses for r in row]
        d = Counter(flat_response)
        mx_freq = 0
        for word,f in d.items():
            mx_freq = max(mx_freq,f)
            
        final = [word for word in d if d[word]==mx_freq]
        final.sort()
        return final[0]