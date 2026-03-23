# LeetCode 1372. Longest ZigZag Path in a Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, state, current_max):
            if not root:
                return
            self.res = max(self.res, current_max)
            if state == 'left':
                dfs(root.right, 'right', current_max + 1)
                dfs(root.left, 'left', 1)
            else:
                dfs(root.left, 'left', current_max + 1)
                dfs(root.right, 'right', 1)
            
        if root.left:
            dfs(root.left, 'left', 1)
        if root.right:
            dfs(root.right, 'right', 1)

        return self.res