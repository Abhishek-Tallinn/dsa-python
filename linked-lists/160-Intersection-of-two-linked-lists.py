# Problem: Leetcode 160 - Intersection of two linked lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Time Complexity: O(m + n) where m and n are the lengths of the two linked lists
# Space Complexity: O(m+n) as we are using two sets to store nodes of both lists.
# Approach: We traverse both linked lists and store their nodes in two separate sets. Then we check for the first common node in both sets which will be the intersection point. If there is no common node, we return None.

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current1 = headA
        current2 = headB
        set1 = set()
        set2 = set()
        while current1:
            if current1 in set2:
                return current1
            set1.add(current1)
            current1 = current1.next
        while current2:
            if current2 in set1:
                return current2
            set2.add(current2)
            current2 = current2.next
        
        return None

        