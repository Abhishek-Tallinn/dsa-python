# Problem: Leetcode 92 - Reverse Linked List II
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-linked-list-ii/description/
# Time Complexity: O(n) where n is the length of linked list
# Space Complexity: O(1) as we just maintain pointers
# Approach: We traverse the linked list and reverse the links between nodes. We use three pointers (current, prev, next_node) to keep track of the nodes and reverse the links 
# between the pointers left and right. we check if last_before left if set. if it is then there is an element before the reversal has to start.
# In that case we can append last_before before the first element of prev pointer. prev maintains the reverse list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        current = head
        prev = None
        for _ in range(left-1):
            prev = current
            current = current.next
        last_before = prev
        tail = current
        prev = None
        for _ in range(right-left+1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        if last_before:
            last_before.next = prev # first part is joined
        else:
            head = prev
            
        tail.next = current

        return head