# Problem: Leetcode 150- Evaluate reverse polish notation
# Difficulty: Medium
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Time Complexity: O(n) as we iterate through the notation elements
# Space Complexity: O(n) as we use a stack to push and pop leements
# Approach: Simple approach of adding elements to stack and when an operator is found then we pop two numbers and perform operation and store result back in the stack
# Since RPN already keeps the precedence we dont need to find precedence or care about paranthesis and we just evaluate the expression.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*',"/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token=='+':
                    stack.append(first+second)
                elif token=="-":
                    stack.append(first-second)
                elif token=="*":
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))

        return stack[0]
            