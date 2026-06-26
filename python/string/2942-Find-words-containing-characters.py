# Problem: Leetcode 2942 - Find words containing characters
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-words-containing-characters/description/
# Time Complexity: O(n)
# Space Complexity: O(n) as we make and iterate over list of strings
# Approach: Since we only have to check membership of one character in each wordof array
# it is actually more efficient to just loop over the words and check it directly instead of converting the word 
# into a set. 


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for idx,word in enumerate(words):
            if x in word:
                ans.append(idx)
        return ans