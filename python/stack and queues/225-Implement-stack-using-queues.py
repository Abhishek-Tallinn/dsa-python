# Problem: Leetcode 225- Implement stack using queues
# Difficulty: Medium
# Link: https://leetcode.com/problems/implement-stack-using-queues/description/
# Time Complexity: O(n) as we push and reverse while other operations are O(1)
# Space Complexity: O(n) as we have a queue
# Approach: We have to simulate a queue so while we append like a normal stack we have to pop from the back also as stack is LIFO but are stuck to use a queue.
# To acheive this when we push an element we always reverse the queue immediately to simulate a stack so that top and pop are available.

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()