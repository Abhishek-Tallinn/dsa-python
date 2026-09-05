# Problem: Leetcode 1021 - Remove outermost parantheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-outermost-parantheses/description/
# Time Complexity: O(1) as we only append and pop to stack
# Space Complexity: O(n) as we have to use a stack
# Approach1: We use a stack where we keep appending elements till we find a condition where open count and close count are equal
# then we pop the stack and append to our answer.
# Approach 2: We keep track of open_count and close_count and also the last original open_idx where a primitive string has started.
# Then we slice from open_idx to the current_idx and and append to answer and set both open and close counts to zero 


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #with stack
        stack = []
        open_count = close_count = 0
        ans = []
        for bracket in s:
            if bracket=='(':
                open_count+=1
                stack.append(bracket)
            if bracket==')':
                stack.append(bracket)
                close_count+=1
                if open_count==close_count:
                    temp = []
                    ans.extend(stack[1:len(stack)-1])
                    stack = []
                    open_count = 0
                    close_count = 0
                    
        return ''.join(ans)
        #return ''.join(''.join(x) for x in ans)
                    
        '''
        without stack
        primitives = []
        open_count = 0 
        open_idx = float('inf')
        for i in range(len(s)):
            if s[i] == '(':
                open_count+=1
                open_idx = min(open_idx,i)
            if s[i]==')':
                if open_count==1:
                    primitives.append(s[open_idx+1:i])
                    open_count = 0
                    open_idx = float('inf')
                else:
                    open_count-=1
        return ''.join(primitives)
        '''