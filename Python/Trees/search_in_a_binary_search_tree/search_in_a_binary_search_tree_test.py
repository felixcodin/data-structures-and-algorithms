import unittest
from search_in_a_binary_search_tree import Solution, TreeNode


def insert_bst(root, node):
    if root is None:
        return node

    cur = root
    while True:
        if node.val < cur.val:
            if cur.left is None:
                cur.left = node
                return root
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = node
                return root
            cur = cur.right


def build_bst_with_refs(values):
    root = None
    refs = {}
    for v in values:
        node = TreeNode(v)
        refs[v] = node
        root = insert_bst(root, node)
    return root, refs


class TestSearchInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree_returns_none(self):
        self.assertIsNone(self.solution.searchBST(None, 5))

    def test_single_node_found(self):
        root = TreeNode(10)
        result = self.solution.searchBST(root, 10)
        self.assertIs(result, root)

    def test_single_node_not_found(self):
        root = TreeNode(10)
        result = self.solution.searchBST(root, 7)
        self.assertIsNone(result)

    def test_find_root_in_multi_node_tree(self):
        root, refs = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 8)
        self.assertIs(result, refs[8])

    def test_find_left_subtree_node(self):
        root, refs = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 3)
        self.assertIs(result, refs[3])

    def test_find_right_subtree_node(self):
        root, refs = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 14)
        self.assertIs(result, refs[14])

    def test_find_leaf_node(self):
        root, refs = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 13)
        self.assertIs(result, refs[13])

    def test_not_found_between_existing_values(self):
        root, _ = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 5)
        self.assertIsNone(result)

    def test_not_found_smaller_than_min(self):
        root, _ = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, -100)
        self.assertIsNone(result)

    def test_not_found_greater_than_max(self):
        root, _ = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 100)
        self.assertIsNone(result)

    def test_found_node_is_subtree_root_reference(self):
        root, refs = build_bst_with_refs([8, 3, 10, 1, 6, 14, 4, 7, 13])
        result = self.solution.searchBST(root, 6)
        self.assertIs(result, refs[6])
        self.assertIs(result.left, refs[4])
        self.assertIs(result.right, refs[7])

    def test_negative_values_tree(self):
        root, refs = build_bst_with_refs([0, -10, 5, -20, -5, 3, 9])
        result = self.solution.searchBST(root, -5)
        self.assertIs(result, refs[-5])

    def test_right_skewed_tree(self):
        root, refs = build_bst_with_refs([1, 2, 3, 4, 5, 6])
        result = self.solution.searchBST(root, 6)
        self.assertIs(result, refs[6])

    def test_left_skewed_tree(self):
        root, refs = build_bst_with_refs([6, 5, 4, 3, 2, 1])
        result = self.solution.searchBST(root, 1)
        self.assertIs(result, refs[1])


if __name__ == "__main__":
    unittest.main()