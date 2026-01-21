# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, value in enumerate(inorder):
            index[value] = i

        def dfs(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_value = preorder[pre_start]
            in_root = index[root_value]
            
            root = TreeNode(root_value)
            nums_left = in_root - in_start


            root.left = dfs(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)
            root.right = dfs(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)

            return root

        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)