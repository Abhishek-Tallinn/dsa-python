# Problem: Leetcode 1081
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
# Time Complexity: O(n + n + n) = O(n)
# Space Complexity: O(n)
# Approach: We make a visited set to track the elements we have seen already as set is best to check for membership. As we iterate throught the string
# we keep adding the elements to the stack if they are not in set. Also we make a hashmap to count the last index of occurrence of each character. if they are in set they are skipped. But while adding the main idea is 
# that if the current char is less than the character at top of stack and the top of stack character occurs again in the string after the index of current char then we pop the stack
# Remember we cannot pop the stack if the top of stack character does not occur again as we need to have all
# the unique character which is also a requirement 

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}#record last indexes
        stack = []
        vis = set()
        for i,char in enumerate(s):
            if char in vis:
                continue
            vis.add(char)
            while stack and stack[-1] > char and last[stack[-1]] > i:
                vis.remove(stack.pop())
            stack.append(char)
            vis.add(char)
            
        return ''.join(stack)