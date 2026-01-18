import unittest
from binary_tree_level_order_traversal import Solution, TreeNode

class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testEmptyTree(self):
        root = None
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [])

    def testSingleNode(self):
        root = TreeNode(1)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1]])

    def testTwoLevels(self):
        # Tree: [3,9,20]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[3], [9, 20]])

    def testThreeLevels(self):
        # Tree: [3,9,20,null,null,15,7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[3], [9, 20], [15, 7]])

    def testOnlyLeftChildren(self):
        # Tree: [1,2,null,3,null,4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2], [3], [4]])

    def testOnlyRightChildren(self):
        # Tree: [1,null,2,null,3,null,4]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2], [3], [4]])

    def testCompleteTree(self):
        # Tree: [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2, 3], [4, 5, 6, 7]])

    def testUnbalancedTree(self):
        # Tree: [1,2,3,4,null,null,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2, 3], [4, 5]])

    def testDeepTree(self):
        # Tree: [5,4,8,11,null,13,4,7,2]
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[5], [4, 8], [11, 13, 4], [7, 2]])


if __name__ == '__main__':
    unittest.main()