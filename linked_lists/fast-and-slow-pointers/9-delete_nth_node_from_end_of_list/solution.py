# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        dummy = ListNode(0, head) # type: ignore
        left = dummy
        right = head

        while(n > 0 and right):
            right = right.next
            n -= 1

        while(right):
            left = left.next
            right = right.next
        
        #Deletion Part
        left.next = left.next.next

        return dummy.next