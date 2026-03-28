import unittest
from collections import deque
from delete_node_in_a_bst import Solution, TreeNode


def insert_bst(root, val):
    if root is None:
        return TreeNode(val)

    cur = root
    while True:
        if val < cur.val:
            if cur.left is None:
                cur.left = TreeNode(val)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(val)
                break
            cur = cur.right
    return root


def build_bst(values):
    root = None
    for v in values:
        root = insert_bst(root, v)
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def serialize_level_order(root):
    if not root:
        return []
    out = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    while out and out[-1] is None:
        out.pop()
    return out


def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)


class TestDeleteNodeInBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_delete_from_empty_tree(self):
        result = self.solution.deleteNode(None, 10)
        self.assertIsNone(result)

    def test_delete_non_existent_key_keeps_tree_unchanged(self):
        root = build_bst([5, 3, 6, 2, 4, 7])
        before = inorder(root)
        result = self.solution.deleteNode(root, 100)

        self.assertEqual(inorder(result), before)
        self.assertTrue(is_valid_bst(result))

    def test_delete_leaf_node(self):
        root = build_bst([5, 3, 6, 2, 4, 7])
        result = self.solution.deleteNode(root, 2)

        self.assertEqual(inorder(result), [3, 4, 5, 6, 7])
        self.assertTrue(is_valid_bst(result))

    def test_delete_node_with_only_left_child(self):
        # Node 3 has only left child 2
        root = build_bst([5, 3, 6, 2])
        result = self.solution.deleteNode(root, 3)

        self.assertEqual(inorder(result), [2, 5, 6])
        self.assertEqual(result.left.val, 2)
        self.assertTrue(is_valid_bst(result))

    def test_delete_node_with_only_right_child(self):
        # Node 3 has only right child 4
        root = build_bst([5, 3, 6, 4])
        result = self.solution.deleteNode(root, 3)

        self.assertEqual(inorder(result), [4, 5, 6])
        self.assertEqual(result.left.val, 4)
        self.assertTrue(is_valid_bst(result))

    def test_delete_root_single_node(self):
        root = TreeNode(1)
        result = self.solution.deleteNode(root, 1)

        self.assertIsNone(result)

    def test_delete_root_with_one_left_child(self):
        root = build_bst([5, 3])
        result = self.solution.deleteNode(root, 5)

        self.assertEqual(inorder(result), [3])
        self.assertEqual(result.val, 3)
        self.assertTrue(is_valid_bst(result))

    def test_delete_root_with_one_right_child(self):
        root = build_bst([5, 7])
        result = self.solution.deleteNode(root, 5)

        self.assertEqual(inorder(result), [7])
        self.assertEqual(result.val, 7)
        self.assertTrue(is_valid_bst(result))

    def test_delete_internal_node_with_two_children(self):
        # Classic case: delete 3 from [5,3,6,2,4,7]
        root = build_bst([5, 3, 6, 2, 4, 7])
        result = self.solution.deleteNode(root, 3)

        self.assertEqual(inorder(result), [2, 4, 5, 6, 7])
        self.assertEqual(serialize_level_order(result), [5, 4, 6, 2, None, None, 7])
        self.assertTrue(is_valid_bst(result))

    def test_delete_root_with_two_children(self):
        # Delete 5 from [5,3,6,2,4,7] -> successor is 6
        root = build_bst([5, 3, 6, 2, 4, 7])
        result = self.solution.deleteNode(root, 5)

        self.assertEqual(inorder(result), [2, 3, 4, 6, 7])
        self.assertEqual(serialize_level_order(result), [6, 3, 7, 2, 4])
        self.assertTrue(is_valid_bst(result))

    def test_delete_with_successor_having_right_child(self):
        # Deleting 30:
        # successor is 35, and 35 has right child 37.
        root = build_bst([50, 30, 70, 20, 40, 60, 80, 35, 45, 37])
        result = self.solution.deleteNode(root, 30)

        self.assertEqual(inorder(result), [20, 35, 37, 40, 45, 50, 60, 70, 80])
        self.assertEqual(result.left.val, 35)
        self.assertEqual(result.left.right.val, 40)
        self.assertEqual(result.left.right.left.val, 37)
        self.assertTrue(is_valid_bst(result))

    def test_multiple_sequential_deletions(self):
        root = build_bst([50, 30, 70, 20, 40, 60, 80])
        for key in [20, 30, 50]:
            root = self.solution.deleteNode(root, key)

        self.assertEqual(inorder(root), [40, 60, 70, 80])
        self.assertTrue(is_valid_bst(root))

    def test_delete_with_negative_values(self):
        root = build_bst([0, -3, 9, -10, -2, 5])
        result = self.solution.deleteNode(root, -3)

        self.assertEqual(inorder(result), [-10, -2, 0, 5, 9])
        self.assertTrue(is_valid_bst(result))


if __name__ == "__main__":
    unittest.main()