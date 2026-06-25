# Problem: Leetcode 3330 - Find the original typed string I
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-original-typed-string-I/description/
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: We just count the number of repetitions as may be she did not intend to type them.
# then we return repeat count + 1 as it may be possible that she wanted to type the original string.


class Solution:
    def possibleStringCount(self, word: str) -> int:
        repeat = 0
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                repeat+=1
        return repeat+1