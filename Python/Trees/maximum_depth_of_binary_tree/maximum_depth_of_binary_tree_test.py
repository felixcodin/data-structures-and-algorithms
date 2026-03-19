import unittest
from maximum_depth_of_binary_tree import TreeNode, Solution


def build_tree(values):
    """
    Build a binary tree from a list using level-order traversal.
    None represents a missing node.
    """
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Add left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        
        # Add right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    
    return root


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # ── Edge cases ─────────────────────────────────────────────────────────

    def testEmptyTree(self):
        root = None
        self.assertEqual(self.solution.maxDepth(root), 0)

    def testSingleNode(self):
        root = build_tree([1])
        self.assertEqual(self.solution.maxDepth(root), 1)

    # ── Balanced trees ────────────────────────────────────────────────────

    def testTwoNodes(self):
        # Tree:   1
        #        /
        #       2
        root = build_tree([1, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def testThreeNodesBalanced(self):
        # Tree:     1
        #         /   \
        #        2     3
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def testFourNodesPartiallyFilled(self):
        # Tree:     1
        #         /   \
        #        2     3
        #       /
        #      4
        root = build_tree([1, 2, 3, 4])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testSevenNodesCompleteBinaryTree(self):
        # Tree:        1
        #         /         \
        #        2           3
        #       / \         / \
        #      4   5       6   7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.maxDepth(root), 3)

    # ── Left-skewed trees ──────────────────────────────────────────────────

    def testLeftSkewedThreeNodes(self):
        # Tree:   1
        #        /
        #       2
        #      /
        #     3
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testLeftSkewedFourNodes(self):
        # Tree:   1
        #        /
        #       2
        #      /
        #     3
        #    /
        #   4
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.maxDepth(root), 4)

    # ── Right-skewed trees ────────────────────────────────────────────────

    def testRightSkewedThreeNodes(self):
        # Tree:   1
        #          \
        #           2
        #            \
        #             3
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testRightSkewedFourNodes(self):
        # Tree:   1
        #          \
        #           2
        #            \
        #             3
        #              \
        #               4
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.maxDepth(root), 4)

    # ── Mixed imbalanced trees ─────────────────────────────────────────────

    def testLeftDeepRightShallow(self):
        # Tree:        1
        #         /         \
        #        2           3
        #       /
        #      4
        #     /
        #    5
        root = build_tree([1, 2, 3, 4, None, None, None, 5])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def testZigzagPattern(self):
        # Tree:        1
        #         /         \
        #        2           3
        #         \         /
        #          4       5
        root = build_tree([1, 2, 3, None, 4, 5])
        self.assertEqual(self.solution.maxDepth(root), 3)

    # ── Values (depth is position-independent) ─────────────────────────────

    def testNegativeValues(self):
        root = build_tree([-1, -2, -3, -4, -5])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testZeroAsRoot(self):
        root = build_tree([0, 0, 0, 0, 0])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testDuplicateValues(self):
        root = build_tree([5, 5, 5, 5, 5, 5, 5])
        self.assertEqual(self.solution.maxDepth(root), 3)

    def testLargeValuesIgnored(self):
        root = build_tree([1000000, 999999, 888888, 777777])
        self.assertEqual(self.solution.maxDepth(root), 3)

    # ── Large trees ────────────────────────────────────────────────────────

    def testDeepLeftSkewedLargeTree(self):
        # Create a tree with depth 10 via left-skew
        values = [i for i in range(10)]
        values_with_none = []
        for v in values:
            values_with_none.append(v)
            values_with_none.append(None)
        values_with_none.pop()  # Remove trailing None
        
        root = build_tree(values_with_none)
        self.assertEqual(self.solution.maxDepth(root), 10)

    def testCompleteBinaryTreeDepth5(self):
        # Complete binary tree with depth 5: 31 nodes (2^5 - 1)
        values = list(range(1, 32))
        root = build_tree(values)
        self.assertEqual(self.solution.maxDepth(root), 5)

    def testCompleteBinaryTreeDepth6(self):
        # Complete binary tree with depth 6: 63 nodes (2^6 - 1)
        values = list(range(1, 64))
        root = build_tree(values)
        self.assertEqual(self.solution.maxDepth(root), 6)

    # ── Sparse trees ───────────────────────────────────────────────────────

    def testSingleLeftChild(self):
        root = build_tree([1, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def testSingleRightChild(self):
        root = build_tree([1, None, 2])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def testOnlyLeftSubtreeDeep(self):
        # Tree:        1
        #         /         \
        #        2           None
        #       / \
        #      3   4
        #     /
        #    5
        root = build_tree([1, 2, None, 3, 4, None, None, 5])
        self.assertEqual(self.solution.maxDepth(root), 4)

    # ── Two-node variations ────────────────────────────────────────────────

    def testTwoNodesLeftChild(self):
        root = build_tree([42, -5])
        self.assertEqual(self.solution.maxDepth(root), 2)

    def testTwoNodesRightChild(self):
        root = build_tree([42, None, 100])
        self.assertEqual(self.solution.maxDepth(root), 2)

    # ── Complex mixed structures ───────────────────────────────────────────

    def testComplexTree1(self):
        # Tree:             1
        #           /               \
        #          2                 3
        #        /   \             /   \
        #       4     5           6     7
        #      /                       /
        #     8                       9
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, 9])
        self.assertEqual(self.solution.maxDepth(root), 4)

    def testComplexTree3(self):
        # Tree:             1
        #           /               \
        #          2                 3
        #            \             /
        #             4           5
        #              \         /
        #               6       7
        #                \       \
        #                 8       9
        root = build_tree([1, 2, 3, None, 4, 5, None, None, 6, 7, None, None, 8, None, 9])
        self.assertEqual(self.solution.maxDepth(root), 5)


if __name__ == "__main__":
    unittest.main()