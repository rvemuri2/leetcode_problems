# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore

        slow, fast = head, head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                break
        
        if not fast or not fast.next:
            return None
        
        slow2 = head
        while(slow2 != slow):
            slow = slow.next
            slow2 = slow2.next
        
        return slow2