# Problem: Leetcode 1408 - String matching in an array
# Difficulty: Medium
# Link: https://leetcode.com/problems/string-matching-in-an-array/description/
# Time Complexity: O(n) - as we reverse the string
# Space Complexity: O(n) as we reverse slice but we can do this with two pointers easily also
# Approach: The input contraints allow us to do a brute force solution so we do a nested loop checking if a string occurs in any other string inside the array
# If it does we append it in our answer array and return ans.

from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if j !=i:
                    if words[i] in words[j]:
                        ans.append(words[i])
        return list(set(ans))