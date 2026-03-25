import unittest
from binary_tree_right_side_view import Solution, TreeNode


def build_tree_level_order(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

    return root


class TestBinaryTreeRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.rightSideView(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.rightSideView(root), [1])

    def test_left_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4 (all left)
        root = build_tree_level_order([1, 2, None, 3, None, 4])
        self.assertEqual(self.solution.rightSideView(root), [1, 2, 3, 4])

    def test_right_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4 (all right)
        root = build_tree_level_order([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.rightSideView(root), [1, 2, 3, 4])

    def test_perfect_binary_tree(self):
        #        1
        #      /   \
        #     2     3
        #    / \   / \
        #   4  5  6   7
        root = build_tree_level_order([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 7])

    def test_sparse_tree_leetcode_style(self):
        # [1,2,3,None,5,None,4]
        root = build_tree_level_order([1, 2, 3, None, 5, None, 4])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4])

    def test_right_missing_left_visible_deeper(self):
        #        1
        #      /   \
        #     2     3
        #      \
        #       5
        #      /
        #     6
        # right side view: [1,3,5,6]
        root = build_tree_level_order([1, 2, 3, None, 5, None, None, 6])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 5, 6])

    def test_mixed_tree_rightmost_from_left_subtree(self):
        #        1
        #      /   \
        #     2     3
        #      \
        #       5
        #        \
        #         8
        # right side view: [1,3,5,8]
        root = build_tree_level_order([1, 2, 3, None, 5, None, None, None, 8])
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 5, 8])

    def test_duplicate_values(self):
        root = build_tree_level_order([1, 1, 1, 1, None, None, 1])
        self.assertEqual(self.solution.rightSideView(root), [1, 1, 1])

    def test_negative_values(self):
        root = build_tree_level_order([-1, -2, -3, None, -5, -6, None])
        self.assertEqual(self.solution.rightSideView(root), [-1, -3, -6])

    def test_two_nodes_left_child(self):
        root = build_tree_level_order([1, 2])
        self.assertEqual(self.solution.rightSideView(root), [1, 2])

    def test_two_nodes_right_child(self):
        root = build_tree_level_order([1, None, 2])
        self.assertEqual(self.solution.rightSideView(root), [1, 2])


if __name__ == "__main__":
    unittest.main()