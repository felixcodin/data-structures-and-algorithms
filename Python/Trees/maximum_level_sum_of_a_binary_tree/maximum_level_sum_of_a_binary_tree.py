# LeetCode 1161. Maximum Level Sum of a Binary Tree

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        res = 0
        mx = float('-inf')
        cur_level = 1

        while q:
            cur_sum = 0
            for i in range(len(q)):
                cur = q.popleft()
                cur_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if cur_sum > mx:
                mx = cur_sum
                res = cur_level
            cur_level += 1

        return res