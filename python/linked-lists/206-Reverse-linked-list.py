# Problem: Leetcode 206 - Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/description/
# Time Complexity: O(n) where n is the length of linked list
# Space Complexity: O(1) as we just maintain pointers
# Approach: We traverse the linked list and reverse the links between nodes. We use three pointers (current, prev, next_node) to keep track of the nodes and reverse the links.
# The above approach has O(1) time complexity



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev= None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        

        return prev