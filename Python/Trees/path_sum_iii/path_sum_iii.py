# LeetCode 437. Path Sum III

from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        self.res = 0
        self.current_sum = defaultdict(int)
        def dfs(root, prev_sum):
            if not root:
                return 

            cur = prev_sum + root.val
            if cur - targetSum in self.current_sum:
                self.res += self.current_sum[cur - targetSum]

            self.current_sum[cur] += 1

            dfs(root.left, cur)
            dfs(root.right, cur)

            self.current_sum[cur] -= 1

        self.current_sum[0] = 1
        dfs(root, 0)
        return self.res