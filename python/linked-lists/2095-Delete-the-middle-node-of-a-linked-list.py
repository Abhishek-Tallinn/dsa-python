# Problem: Leetcode 2095 - Delete the Middle Node of a Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Time Complexity: O(n) - need to traverse the list. 
# Space Complexity: O(1) - no new data structure
# Approach1: Traverse the list once to find its length and then find middle node. then traverse upto the node before that and disconnect the target node.
# Approach2: Use two pointers, one slow and one fast. Move the fast pointer twice as fast as the slow pointer. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node. Then we can delete the middle node by changing the next pointer of the previous node to skip the middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        current = head
        l = 0
        while current:
            l+=1
            current=current.next
        middle = l//2
        if middle == 0:
            return head.next
        current = head
        for i in range(middle-1):
            current = current.next
        current.next = current.next.next
        return head
    
        '''
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev:
            return head.next
        prev.next = slow.next
        return head
        '''