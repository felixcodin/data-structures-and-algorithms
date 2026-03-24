import unittest
from lowest_common_ancestor_of_a_binary_tree import Solution, TreeNode



def build_classic_tree():
    # Tree:
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6   2 0   8
    #       / \
    #      7   4
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n1.left = n0
    n1.right = n8
    n2.left = n7
    n2.right = n4

    return n3, {
        3: n3,
        5: n5,
        1: n1,
        6: n6,
        2: n2,
        0: n0,
        8: n8,
        7: n7,
        4: n4,
    }


def build_non_bst_tree():
    # Tree (intentionally not BST):
    #         10
    #       /    \
    #     20      5
    #    /  \    / \
    #   1   15  30  2
    n10 = TreeNode(10)
    n20 = TreeNode(20)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n15 = TreeNode(15)
    n30 = TreeNode(30)
    n2 = TreeNode(2)

    n10.left = n20
    n10.right = n5
    n20.left = n1
    n20.right = n15
    n5.left = n30
    n5.right = n2

    return n10, {
        10: n10,
        20: n20,
        5: n5,
        1: n1,
        15: n15,
        30: n30,
        2: n2,
    }


class TestLowestCommonAncestorOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_nodes_in_different_subtrees_lca_is_root(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[5], nodes[1])
        self.assertIs(result, nodes[3])

    def test_both_nodes_in_left_subtree(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[6], nodes[4])
        self.assertIs(result, nodes[5])

    def test_both_nodes_in_right_subtree(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[0], nodes[8])
        self.assertIs(result, nodes[1])

    def test_one_node_is_ancestor_of_other(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[5], nodes[4])
        self.assertIs(result, nodes[5])

    def test_root_is_one_of_targets(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[3], nodes[7])
        self.assertIs(result, nodes[3])

    def test_same_node_for_p_and_q(self):
        root, nodes = build_classic_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[2], nodes[2])
        self.assertIs(result, nodes[2])

    def test_two_node_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        result = self.solution.lowestCommonAncestor(root, root, root.left)
        self.assertIs(result, root)

    def test_left_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4 (all left)
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n1.left = n2
        n2.left = n3
        n3.left = n4

        result = self.solution.lowestCommonAncestor(n1, n3, n4)
        self.assertIs(result, n3)

    def test_right_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4 (all right)
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n1.right = n2
        n2.right = n3
        n3.right = n4

        result = self.solution.lowestCommonAncestor(n1, n2, n4)
        self.assertIs(result, n2)

    def test_non_bst_structure_still_correct(self):
        root, nodes = build_non_bst_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[1], nodes[15])
        self.assertIs(result, nodes[20])

    def test_non_bst_cross_subtrees(self):
        root, nodes = build_non_bst_tree()
        result = self.solution.lowestCommonAncestor(root, nodes[15], nodes[30])
        self.assertIs(result, nodes[10])

    def test_empty_tree_returns_none(self):
        result = self.solution.lowestCommonAncestor(None, TreeNode(1), TreeNode(2))
        self.assertIsNone(result)

    def test_one_node_not_present_returns_found_node_with_current_logic(self):
        root, nodes = build_classic_tree()
        missing = TreeNode(999)
        result = self.solution.lowestCommonAncestor(root, nodes[6], missing)
        self.assertIs(result, nodes[6])


if __name__ == "__main__":
    unittest.main()