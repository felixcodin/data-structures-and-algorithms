# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        mn = min(p.val, q.val)
        mx = max(p.val, q.val)
        while curr:
            if curr.val > mx:
                curr = curr.left
            elif curr.val < mn:
                curr = curr.right
            else:
                break
        return curr