# Problem: Leetcode 2130 - Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Time Complexity: O(n) - need to traverse the list. 
# Space Complexity: O(1) or O(n) - depending on approach
# Approach1: Traverse the list with two pointers slow and fast to find the middle. the reverse the second half and then run two pointers first and second in parallel and add all the values. 
# Approach2: Simpler approach but with O(n) space complexity. We traverse the linked list and collect the values in a list and then simple add the alternates with two pointers. 



from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #O(1) solution
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        first = head
        second = prev
        mx = 0
        while first and second:
            mx = max(mx,first.val+second.val)
            first = first.next
            second = second.next
        return mx



        '''
        l = []
        current = head
        while current:
            l.append(current.val)
            current=current.next
        left = 0
        right = len(l)-1
        mx = 0
        while left<right:
            mx = max(mx, l[left]+l[right])
            left+=1
            right-=1
        return mx
        '''