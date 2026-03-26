import unittest
from maximum_level_sum_of_a_binary_tree import Solution, TreeNode


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


class TestMaximumLevelSumOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = build_tree_level_order([5])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_leetcode_style_example(self):
        # [1,7,0,7,-8,None,None]
        # Level sums: 1, 7, -1 -> answer = 2
        root = build_tree_level_order([1, 7, 0, 7, -8, None, None])
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_perfect_tree_max_at_deepest_level(self):
        # [1,2,3,4,5,6,7]
        # Level sums: 1, 5, 22 -> answer = 3
        root = build_tree_level_order([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.maxLevelSum(root), 3)

    def test_all_negative_values(self):
        # [-1,-2,-3,-4,-5]
        # Level sums: -1, -5, -9 -> answer = 1
        root = build_tree_level_order([-1, -2, -3, -4, -5])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_tie_returns_smallest_level(self):
        # [5,2,3]
        # Level sums: 5, 5 -> tie => smallest level = 1
        root = build_tree_level_order([5, 2, 3])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_right_skewed_tree(self):
        # [1,None,2,None,3,None,4]
        # Level sums: 1,2,3,4 -> answer = 4
        root = build_tree_level_order([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.maxLevelSum(root), 4)

    def test_left_skewed_tree(self):
        # [4,3,None,2,None,1]
        # Level sums: 4,3,2,1 -> answer = 1
        root = build_tree_level_order([4, 3, None, 2, None, 1])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_sparse_tree_max_middle_level(self):
        # [1,2,3,4,5,None,8,None,None,6,7]
        # Level sums: 1,5,17,13 -> answer = 3
        root = build_tree_level_order([1, 2, 3, 4, 5, None, 8, None, None, 6, 7])
        self.assertEqual(self.solution.maxLevelSum(root), 3)

    def test_all_zero_values_tie(self):
        # [0,0,0,0,None,None,0]
        # Level sums: 0,0,0 -> tie => smallest level = 1
        root = build_tree_level_order([0, 0, 0, 0, None, None, 0])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_large_magnitude_values(self):
        # [100000,-100000,1,2,3,4,5]
        # Level sums: 100000, -99999, 14 -> answer = 1
        root = build_tree_level_order([100000, -100000, 1, 2, 3, 4, 5])
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_max_at_second_level(self):
        # [1,10,10,-1,-1,-1,-1]
        # Level sums: 1,20,-4 -> answer = 2
        root = build_tree_level_order([1, 10, 10, -1, -1, -1, -1])
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_none_root_current_behavior_raises(self):
        # Current implementation initializes queue with [None] and accesses cur.val.
        with self.assertRaises(AttributeError):
            self.solution.maxLevelSum(None)


if __name__ == "__main__":
    unittest.main()