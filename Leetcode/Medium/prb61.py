# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        size, tail = 1, head
        while tail.next:
            size += 1
            tail = tail.next

        k = k % size
        if k == 0:
            return head

        curr = head
        for _ in range(size - k - 1):
            curr = curr.next
        temp = curr.next
        curr.next = None
        tail.next = head
        return temp