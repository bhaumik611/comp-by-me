# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from typing import Optional, ListNode
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # First, let's determine the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Normalize k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # Find the new tail: (length - k - 1)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # The new head is the next node after the new tail
        new_head = new_tail.next

        # Break the link to form the new list
        new_tail.next = None

        # Connect the old tail to the old head
        current.next = head

        return new_head