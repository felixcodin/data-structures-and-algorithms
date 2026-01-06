# LeetCode 2181. Merge Nodes in Between Zeros

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        prev = head
        while curr is not None:
            curr = curr.next
            if curr is not None and curr.val == 0:
                curr = curr.next
                prev.next = curr
                prev = prev.next
            elif curr is None:
                break
            else:
                prev.val += curr.val

        return head