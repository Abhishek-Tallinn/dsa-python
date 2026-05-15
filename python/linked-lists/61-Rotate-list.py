# Problem: Leetcode 61 - Rotate List
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-list/description/
# Time Complexity: O(n) where n is the length of linked list
# Space Complexity: O(1) as we just maintain pointers
# Approach: We traverse the linked list and find its length and make it circular. Then we find the number of effective rotations by taking modulus. Then we find the new tail and set new head as the next of new Tail and return the new head.
# The above approach has O(1) time complexity
# Approach2: We can copy the nodev values in a list and rotate the list as per requirement. Then we make each value in list to a linked list node and return the head. This way is easier but and time complexity is O(n) but the space complexity is O(n) as we use an extra list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # in-place solution
        # base case in linked list
        if not head or not head.next:
            return head
        #length compute
        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next
        k = k%length
        if k==0:
            return head
        # k will always be in the range of the length so we can use a for loop
        tail.next = head
        steps = length - k - 1
        tail2 = head
        for _ in range(steps):
            tail2 = tail2.next
        head2 = tail2.next
        tail2.next = None
        return head2
        

        '''
        O(n) and O(n) solution
        current = head
        l = []
        count = 0
        while current:
            l.append(current.val)
            count+=1
            current = current.next
        if count == 0:
            return head
        k%=count
        l = l[-k:]+l[:-k]
        head2 = ListNode(l[0])
        prev = head2
        for node in l[1:]:
            new = ListNode(node)
            prev.next = new
            prev = new
        return head2
        '''