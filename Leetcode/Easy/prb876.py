from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next
        return l


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head: Optional[ListNode]) -> int:
        count = 0
        itr = head
        while itr:
            count += 1
            itr = itr.next
        return count

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = self.get_length(head) // 2
        count = 0
        itr = head
        while itr:
            if count == mid:
                return itr
            count += 1
            itr = itr.next
'''