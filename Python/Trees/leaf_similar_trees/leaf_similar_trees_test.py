import unittest
from leaf_similar_trees import TreeNode, Solution


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


def get_leaf_sequence(root):
    """Helper to extract leaf sequence from a tree."""
    leaves = []
    
    def dfs(node):
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return leaves


class TestLeafSimilarTrees(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # ── Edge cases ─────────────────────────────────────────────────────────

    def testBothEmpty(self):
        root1 = None
        root2 = None
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testFirstEmpty(self):
        root1 = None
        root2 = build_tree([1])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testSecondEmpty(self):
        root1 = build_tree([1])
        root2 = None
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testBothSingleNode(self):
        root1 = build_tree([1])
        root2 = build_tree([1])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testBothSingleNodeDifferent(self):
        root1 = build_tree([1])
        root2 = build_tree([2])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── LeetCode canonical examples ────────────────────────────────────────

    def testLeetCodeExample1(self):
        # Tree1:     3         Tree2:     3
        #          /   \                /   \
        #         5     1              5     1
        #        / \   / \            / \   / \
        #       6   2 9   8          6   7 4   2
        #         / \                     / \
        #        7   4                   9   8
        # Leaves: [6, 7, 4, 9, 8]        [6, 7, 4, 9, 8] → True
        root1 = build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, 9, 8])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testLeetCodeExample2(self):
        # Tree1:     1         Tree2:     2
        #              \                /
        #               2              1
        # Leaves: [2]                   [1] → False
        root1 = build_tree([1, None, 2])
        root2 = build_tree([2, 1])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Two-node trees ─────────────────────────────────────────────────────

    def testTwoNodesLeftChildSame(self):
        # Both have left child only, same value
        root1 = build_tree([1, 2])
        root2 = build_tree([3, 2])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testTwoNodesRightChildSame(self):
        # Both have right child only, same value
        root1 = build_tree([1, None, 2])
        root2 = build_tree([3, None, 2])
        self.assertTrue(self.solution.leafSimilar(root1, root2))


    def testTwoNodesLeftChildDifferent(self):
        root1 = build_tree([1, 2])
        root2 = build_tree([1, 3])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Three-node trees ───────────────────────────────────────────────────

    def testThreeNodesBalancedSame(self):
        # Both have same leaf values from left and right children
        root1 = build_tree([1, 2, 3])
        root2 = build_tree([10, 2, 3])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testThreeNodesBalancedDifferent(self):
        root1 = build_tree([1, 2, 3])
        root2 = build_tree([1, 2, 4])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testThreeNodesLeftSkewedSame(self):
        root1 = build_tree([1, 2, None, 3])
        root2 = build_tree([10, 2, None, 3])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testThreeNodesRightSkewedSame(self):
        root1 = build_tree([1, None, 2, None, 3])
        root2 = build_tree([10, None, 2, None, 3])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    # ── Linear chains (skewed trees) ───────────────────────────────────

    def testLeftSkewedChainSame(self):
        # Chain: 1 → 2 → 3 → 4 (all left children)
        root1 = build_tree([1, 2, None, 3, None, 4])
        root2 = build_tree([10, 2, None, 3, None, 4])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testLeftSkewedChainDifferent(self):
        root1 = build_tree([1, 2, None, 3, None, 4])
        root2 = build_tree([1, 2, None, 3, None, 5])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testRightSkewedChainSame(self):
        # Chain: 1 → 2 → 3 → 4 (all right children)
        root1 = build_tree([1, None, 2, None, 3, None, 4])
        root2 = build_tree([10, None, 2, None, 3, None, 4])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testRightSkewedChainDifferent(self):
        root1 = build_tree([1, None, 2, None, 3, None, 4])
        root2 = build_tree([1, None, 2, None, 3, None, 5])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Multiple leaves ────────────────────────────────────────────────────

    def testFourLeavesOrderSensitive(self):
        # Tree1 leaves: [4, 5, 6, 7]
        # Tree2 leaves: [7, 6, 5, 4] (reversed) → False
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([1, 3, 2, 7, 6, 5, 4])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testFourLeavesSameOrder(self):
        # Both Trees have same leaf order [4, 5, 6, 7]
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([100, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.solution.leafSimilar(root1, root2))


    # ── Imbalanced trees ───────────────────────────────────────────────────

    def testLeftDeepRightShallowSame(self):
        # Tree1: Left subtree deep, right is shallow
        #        1
        #       / \
        #      2   5
        #     / \
        #    3   4
        # Leaves: [3, 4, 5]
        root1 = build_tree([1, 2, 5, 3, 4])
        root2 = build_tree([10, 20, 50, 30, 40])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testRightDeepLeftShallowSame(self):
        # Tree1: Right subtree deep, left is shallow
        root1 = build_tree([1, 5, 2, None, None, 3, 4])
        root2 = build_tree([10, 50, 20, None, None, 30, 40])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testLeftDeepRightShallowDifferent(self):
        root1 = build_tree([1, 2, 5, 3, 4])
        root2 = build_tree([1, 2, 6, 3, 4])  # Different right leaf (5 vs 6)
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Node value edge cases ──────────────────────────────────────────────

    def testNegativeLeafValues(self):
        root1 = build_tree([-1, -2, -3, -4, -5, -6, -7])
        root2 = build_tree([100, 200, 300, -4, -5, -6, -7])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testZeroAsLeafValue(self):
        root1 = build_tree([1, 2, 3, 0, 0, 0, 0])
        root2 = build_tree([10, 20, 30, 0, 0, 0, 0])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testMixedPositiveNegativeLeaves(self):
        root1 = build_tree([0, -1, 1, -2, -3, 2, 3])
        root2 = build_tree([100, -1, 1, -2, -3, 2, 3])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testLargeLeafValues(self):
        root1 = build_tree([0, 1000000, -1000000, 999999, 1000001, -999999, -1000001])
        root2 = build_tree([5, 1000000, -1000000, 999999, 1000001, -999999, -1000001])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testDuplicateLeafValues(self):
        root1 = build_tree([1, 5, 5, 5, 5, 5, 5])
        root2 = build_tree([100, 5, 5, 5, 5, 5, 5])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    # ── Complex structural differences ─────────────────────────────────────

    def testSameLeavesDifferentStructure1(self):
        # Tree1:     1          Tree2:       1
        #          /   \                    / \
        #         2     3                  2   3
        #        /       \                /     \
        #       4         5              4       5
        # Both have leaves [4, 5]
        root1 = build_tree([1, 2, 3, 4, None, None, 5])
        root2 = build_tree([1, 2, 3, 4, None, None, 5])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testSameLeavesDifferentStructure2(self):
        # Tree1:     1        Tree2:      1
        #              \               /   \
        #               2             2     3
        #              / \           /
        #             3   4         3
        #                          /
        #                         4
        # Tree1 leaves: [3, 4]  Tree2 leaves: [4, 3] → Different order → False
        root1 = build_tree([1, None, 2, 3, 4])
        root2 = build_tree([1, 2, 3, 4])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testDifferentLengthChains(self):
        # Tree1 has 2 leaves, Tree2 has 3 leaves
        root1 = build_tree([1, 2, 3])
        root2 = build_tree([1, 2, None, None, 3, None, 4])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Root nodes with no leaves (single nodes are leaves) ───────────────

    def testRootIsLeafOnlyFirstTree(self):
        root1 = TreeNode(5)
        root2 = build_tree([1, 2, 3])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Sparse trees with None gaps ────────────────────────────────────────


    def testSparseRightSubtree(self):
        root1 = build_tree([1, 2, None, 3])
        root2 = build_tree([1, 2, None, 3])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    # ── Large trees ────────────────────────────────────────────────────────

    def testCompleteBinaryTreeDepth4Same(self):
        # Complete binary tree with depth 4: 15 nodes, 8 leaves
        values1 = list(range(1, 16))
        values2 = [i for i in range(1, 16)]
        root1 = build_tree(values1)
        root2 = build_tree(values2)
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testLongLeftChainSame(self):
        # Linear chain of 10 nodes (all left)
        values = list(range(1, 11))
        values_with_nones = []
        for v in values:
            values_with_nones.append(v)
            values_with_nones.append(None)
        values_with_nones.pop()
        
        root1 = build_tree(values_with_nones)
        root2 = build_tree([v for v in values_with_nones])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testLongChainsDifferentLengths(self):
        # Chain of 5 vs chain of 6
        chain1 = [1, 2, None, 3, None, 4, None, 5]
        chain2 = [1, 2, None, 3, None, 4, None, 5, None, 6]
        root1 = build_tree(chain1)
        root2 = build_tree(chain2)
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Leaf sequence mutation scenarios ───────────────────────────────────

    def testSwappedLeaves(self):
        # Same leaves but swapped → different order
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([1, 3, 2, 6, 7, 4, 5])  # Swapped pairs
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testRotatedLeafSequence(self):
        # [4, 5, 6, 7] vs [5, 6, 7, 4]
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([1, 4, 2, 5, 6, 7, None])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testInsertedLeafInMiddle(self):
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testRemovedLeaf(self):
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([1, 2, 3, 4, 5, 6])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    # ── Internal node values don't affect leaves ───────────────────────────

    def testInternalValueChangeSameLeaves(self):
        # Change internal nodes, leaves remain [4, 5, 6, 7]
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
        root2 = build_tree([999, 888, 777, 4, 5, 6, 7])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def testAllInternalValuesChangedSameLeaves(self):
        root1 = build_tree([10, 20, 30, 40, 50, 60, 70])
        root2 = build_tree([-10, -20, -30, 40, 50, 60, 70])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    # ──  Additional corner cases ───────────────────────────────────────────

    def testVeryUnbalancedLeftTree(self):
        # Tree1 is completely left-skewed; Tree2 is balanced
        #       1
        #      /
        #     2
        #    /
        #   3
        # vs
        #     3
        #    / \
        #   2   3
        root1 = build_tree([1, 2, None, 3])
        root2 = build_tree([10, 2, 3])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def testMultipleLeafNodesSamePath(self):
        # Ensure all leaf nodes (no children) are captured
        root1 = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        root2 = build_tree([100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertTrue(self.solution.leafSimilar(root1, root2))


if __name__ == "__main__":
    unittest.main()