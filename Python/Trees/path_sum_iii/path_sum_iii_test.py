# Unit Tests for LeetCode 437. Path Sum III

import unittest
from path_sum_iii import TreeNode, Solution


def build_tree(values: list) -> TreeNode:
    """Helper to build a binary tree from a level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class TestPathSumIII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # ------------------------------------------------------------------
    # LeetCode examples
    # ------------------------------------------------------------------

    def test_example1(self):
        r"""
        Tree:
                 10
                /  \
               5   -3
              / \    \
             3   2   11
            / \   \
           3  -2   1
        targetSum = 8  →  3 paths
        """
        root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(self.solution.pathSum(root, 8), 3)

    def test_example2(self):
        """
        Tree: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        targetSum = 22  →  3 paths
        """
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertEqual(self.solution.pathSum(root, 22), 3)

    # ------------------------------------------------------------------
    # Edge cases
    # ------------------------------------------------------------------

    def test_empty_tree(self):
        """An empty tree has no paths."""
        self.assertEqual(self.solution.pathSum(None, 0), 0)

    def test_single_node_matches(self):
        """Single node whose value equals targetSum."""
        root = TreeNode(5)
        self.assertEqual(self.solution.pathSum(root, 5), 1)

    def test_single_node_no_match(self):
        """Single node whose value differs from targetSum."""
        root = TreeNode(3)
        self.assertEqual(self.solution.pathSum(root, 5), 0)

    def test_target_zero(self):
        r"""
        Paths that sum to zero require negative values on the path.
        Tree:
             1
            / \
           -1   2
        Paths summing to 0: [1, -1]  →  1 path
        """
        root = build_tree([1, -1, 2])
        self.assertEqual(self.solution.pathSum(root, 0), 1)

    def test_negative_target(self):
        """Negative targetSum should still be found correctly."""
        root = build_tree([-1, -2, -3])
        # Paths: [-1,-2]=-3, [-1,-3]=-4, [-1]=-1, [-2]=-2, [-3]=-3
        # Paths summing to -3: [-1,-2] and [-3]  →  2 paths
        self.assertEqual(self.solution.pathSum(root, -3), 2)

    def test_all_nodes_same_value(self):
        r"""
        Tree:
             1
            / \
           1   1
        targetSum = 1  →  3 paths (root, root.left, root.right)
        """
        root = build_tree([1, 1, 1])
        self.assertEqual(self.solution.pathSum(root, 1), 3)

    def test_path_not_from_root(self):
        r"""
        Path does not have to start from the root.
        Tree:
             1
              \
               2
                \
                 3
        targetSum = 5  →  [2, 3]  →  1 path
        """
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.pathSum(root, 5), 1)

    def test_large_negative_values(self):
        """Handles large negative node values correctly."""
        root = build_tree([-1000, -1000, -1000])
        # Paths summing to -2000: [-1000,-1000] (left) and [-1000,-1000] (right)  →  2 paths
        self.assertEqual(self.solution.pathSum(root, -2000), 2)

    def test_no_valid_path(self):
        """targetSum cannot be reached by any path."""
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.pathSum(root, 100), 0)

    def test_every_node_is_a_path(self):
        r"""
        Tree:
             0
            / \
           0   0
        targetSum = 0  →  all single nodes + root-to-child paths all sum to 0  →  5 paths
        Paths: [0], [0,0] (left), [0] (left), [0,0] (right), [0] (right)
        """
        root = build_tree([0, 0, 0])
        self.assertEqual(self.solution.pathSum(root, 0), 5)


if __name__ == "__main__":
    unittest.main()
