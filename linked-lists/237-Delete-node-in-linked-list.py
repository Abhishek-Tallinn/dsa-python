# Problem: Leetcode 237 - Delete Node in a Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Time Complexity: O(1) - no iteration just in place modification
# Space Complexity: O(1) - no new data structure
# Approach: Since we are not given the head of the linked list, we cannot traverse to find the node to be deleted. Instead, we copy the value of the next node to the current node and then delete the next node.
# We then traverse the list and remove nodes with the specified value.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
