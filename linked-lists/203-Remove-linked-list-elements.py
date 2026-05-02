# Problem: Leetcode 203 - Remove Linked List Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-linked-list-elements/description/
# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(1) as we are using only a constant amount of extra space
# Approach: We use a dummy node to handle the case where the head node needs to be removed. 
# We then traverse the list and remove nodes with the specified value.
# Dummy node is required as the head might need removal itself. The usual logic of current.next = current.next.next to drop a node is only for middle of list

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next