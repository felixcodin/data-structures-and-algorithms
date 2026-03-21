import unittest
from count_good_nodes_in_binary_tree import TreeNode, Solution


def build_tree(values: list) -> TreeNode:
    """Build a binary tree from a level-order list (None = missing node).

    Matches LeetCode's serialisation format: None entries are placeholders
    for absent nodes and do NOT occupy a slot in the queue.
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        # right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


class TestGoodNodes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # ------------------------------------------------------------------
    # LeetCode example cases
    # ------------------------------------------------------------------

    def test_example_1(self):
        # Tree: [3, 1, 4, 3, None, 1, 5]
        #        3
        #       / \
        #      1   4
        #     /   / \
        #    3   1   5
        # Good nodes: 3 (root), 3 (left-left), 4, 5  => 4
        root = build_tree([3, 1, 4, 3, None, 1, 5])
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_example_2(self):
        # Tree: [3, 3, None, 4, 2]
        #    3
        #   /
        #  3
        # / \
        # 4   2
        # Good nodes: 3 (root), 3 (left child), 4  => 3
        root = build_tree([3, 3, None, 4, 2])
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_example_3(self):
        # Single node
        root = build_tree([1])
        self.assertEqual(self.solution.goodNodes(root), 1)

    # ------------------------------------------------------------------
    # Edge cases
    # ------------------------------------------------------------------

    def test_single_node_negative(self):
        root = build_tree([-1])
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_all_same_values(self):
        # Every node equals the running max -> all are good
        root = build_tree([2, 2, 2, 2, 2])
        self.assertEqual(self.solution.goodNodes(root), 5)

    def test_strictly_increasing_left_path(self):
        # 1 -> 2 -> 3 -> 4 (all good)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_strictly_decreasing_left_path(self):
        # 4 -> 3 -> 2 -> 1 (only root is good)
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_right_skewed_all_good(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(7)
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_right_skewed_none_good_except_root(self):
        root = TreeNode(10)
        root.right = TreeNode(5)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_negative_values(self):
        # [-3, -5, -1] -> root (-3) is good, -5 < -3 not good, -1 > -3 good
        root = build_tree([-3, -5, -1])
        self.assertEqual(self.solution.goodNodes(root), 2)

    def test_mixed_positive_negative(self):
        # Tree: [5, -2, 8, -3, 4]
        #         5
        #        / \
        #      -2   8
        #      / \
        #    -3   4
        # Path to -2: max=5, -2 < 5 -> not good
        # Path to 8:  max=5, 8 >= 5 -> good
        # Path to -3: max=5, -3 < 5 -> not good
        # Path to 4:  max=5, 4 < 5  -> not good
        # Good: 5 (root), 8 => 2
        root = build_tree([5, -2, 8, -3, 4])
        self.assertEqual(self.solution.goodNodes(root), 2)

    def test_all_nodes_good(self):
        # Perfect BST-like ascending on both sides
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_large_balanced_tree(self):
        # A balanced tree where root value is very small -> many good nodes
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        # Good: 1?, no — 2>1 yes, 3>1 yes, 4>2 yes, 5>2 yes, 6>3 yes, 7>3 yes
        # All 7 are good
        self.assertEqual(self.solution.goodNodes(root), 7)


if __name__ == "__main__":
    unittest.main()
