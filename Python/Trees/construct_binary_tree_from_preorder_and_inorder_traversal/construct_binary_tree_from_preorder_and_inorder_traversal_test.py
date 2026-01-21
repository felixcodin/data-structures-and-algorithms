import unittest
from construct_binary_tree_from_preorder_and_inorder_traversal import Solution, TreeNode

class TestConstructBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tree_to_list(self, root):
        """Helper function to convert tree to level order list for comparison"""
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    def testSingleNode(self):
        preorder = [1]
        inorder = [1]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1])

    def testTwoNodesLeftChild(self):
        preorder = [1, 2]
        inorder = [2, 1]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, 2])

    def testTwoNodesRightChild(self):
        preorder = [1, 2]
        inorder = [1, 2]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, None, 2])

    def testThreeNodesBalanced(self):
        preorder = [3, 9, 20]
        inorder = [9, 3, 20]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [3, 9, 20])

    def testExampleTree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [3, 9, 20, None, None, 15, 7])

    def testOnlyLeftChildren(self):
        preorder = [1, 2, 3, 4]
        inorder = [4, 3, 2, 1]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, 2, None, 3, None, 4])

    def testOnlyRightChildren(self):
        preorder = [1, 2, 3, 4]
        inorder = [1, 2, 3, 4]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, None, 2, None, 3, None, 4])

    def testCompleteTree(self):
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, 2, 3, 4, 5, 6, 7])

    def testUnbalancedTree(self):
        preorder = [1, 2, 4, 3, 5]
        inorder = [4, 2, 1, 3, 5]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, 2, 3, 4, None, None, 5])

    def testLargerTree(self):
        preorder = [5, 4, 11, 7, 2, 8, 13, 30]
        inorder = [7, 11, 2, 4, 5, 13, 8, 30]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [5, 4, 8, 11, None, 13, 30, 7, 2])

    def testNegativeValues(self):
        preorder = [-10, -3, 0, 5, 9]
        inorder = [0, -3, 5, -10, 9]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [-10, -3, 9, 0, 5])

    def testDuplicateStructure(self):
        preorder = [1, 2, 3, 4, 5]
        inorder = [3, 2, 4, 1, 5]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), [1, 2, 5, 3, 4])


if __name__ == '__main__':
    unittest.main()