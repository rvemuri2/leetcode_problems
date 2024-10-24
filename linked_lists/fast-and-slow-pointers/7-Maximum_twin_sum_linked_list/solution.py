# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int: # type: ignore
        sum1 = 0

        slow, fast = head, head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        ptr1, ptr2 = head, prev
        while(ptr2):
            sum1 = max(sum1, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return sum1