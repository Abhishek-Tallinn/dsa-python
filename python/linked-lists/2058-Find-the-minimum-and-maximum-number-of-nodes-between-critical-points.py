from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        current = head
        first_c_idx = prev_c_idx = float('inf')
        prev = None
        mn = float('inf')
        mx = -1
        idx = 0
        l = []
        while current.next:
            if not prev:
                prev = current
                idx+=1
                current = current.next
                continue
            if (current.val > prev.val and current.val > current.next.val) or (current.val < prev.val and current.val < current.next.val):
                if first_c_idx==float('inf'):
                    first_c_idx = idx 
                    prev_c_idx = idx
                    idx+=1
                    prev = current
                    current=current.next
                    continue
                mn = min(mn,abs(idx-prev_c_idx))
                mx = max(mx,idx-first_c_idx)
                prev_c_idx = idx
            idx+=1
            prev = current
            current = current.next
        return [-1,mx] if mn == float('inf') else [mn,mx] 