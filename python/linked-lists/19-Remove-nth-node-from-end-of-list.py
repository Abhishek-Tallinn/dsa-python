# Problem: Leetcode 19 - Remove Nth Node From End of List
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Time Complexity: O(n) where n is the length of linked list
# Space Complexity: O(1) as we just maintain pointers
# Approach: We traverse the linked list and first find its length and then by doing length - n find the index of the element to be deleted.
# The with traditional approach we iterate till target_node-1 and set the next of the previous node to next.next.
# Approach2: We can also have another approach where we have we use a fast and slow pointer and move the fast pointer n steps ahead and then move both pointers one step at a time until the fast pointer reaches the end. Then the slow pointer will be at the node to be deleted. We can then set the next of slow pointer to next.next and return head. This approach also has O(n) time complexity but we do not need to calculate the length of linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        l=0
        while current:
            l+=1
            current=current.next
        if l == 1:
            return None
        #now we have length
        node_to_delete = l-n
        idx = 0
        if node_to_delete==0:
            head = head.next
            return head
        current2 = head
        prev = head
        for _ in range(node_to_delete):
            prev = current2
            current2=current2.next
        prev.next = current2.next
        return head