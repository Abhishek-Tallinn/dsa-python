# Problem: Leetcode 402 - Remove K digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-k-digits/description/
# Time Complexity: O(n) as we iterate through the list
# Space Complexity: O(n) as we use a stack which can have the elements of the string.
# Approach: Since technically any digit can be removed, we use a stack with greedy approach that if there is any digit which is greater than the digit to its right we just remove it.
# We maintain a monotonic stack that only keep elements in increaing order till k>0. Once limit of  k is reach the rest elements are appended to the stack.
# then we just return the stack as a array while stripping any 0's on the left.


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # if still need to remove digits
        while k > 0:
            stack.pop()
            k -= 1

        # build result and remove leading zeros
        print("Stack is", stack)
        result = ''.join(stack).lstrip('0')

        return result if result else "0"