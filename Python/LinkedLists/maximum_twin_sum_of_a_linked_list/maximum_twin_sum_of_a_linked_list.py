# LeetCode 2130. Maximum Twin Sum of a Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_node = []

        cur = head
        while cur:
            list_node.append(cur.val)
            cur = cur.next
        
        n = len(list_node)

        mx = 0
        for i in range(n//2):
            mx = max(mx, list_node[i] + list_node[n-i-1])
            
        return mx