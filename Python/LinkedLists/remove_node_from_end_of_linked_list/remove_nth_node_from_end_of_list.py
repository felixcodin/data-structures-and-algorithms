# LeetCode 19. Remove Nth Node From End of List

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for i in range(n):
            first = first.next

        if first is None:
            head = second.next

        prev = second
        while first is not None:
            first = first.next
            prev = second
            second = second.next

        prev.next = second.next

        return head
        