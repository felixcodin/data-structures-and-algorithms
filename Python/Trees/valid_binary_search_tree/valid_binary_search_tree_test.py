import unittest
from valid_binary_search_tree import Solution, TreeNode

class TestValidBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testEmptyTree(self):
        root = None
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testSingleNode(self):
        root = TreeNode(1)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testValidBSTTwoNodes(self):
        # Tree: [2,1,3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testInvalidBSTLeftGreater(self):
        # Tree: [5,1,4,null,null,3,6]
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)

    def testValidBSTMultipleLevels(self):
        # Tree: [5,1,7,null,null,6,8]
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(8)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testInvalidBSTDuplicateValues(self):
        # Tree: [2,2,2]
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)

    def testInvalidBSTRightChild(self):
        # Tree: [5,4,6,null,null,3,7]
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)

    def testValidBSTOnlyLeftChildren(self):
        # Tree: [5,3,null,1]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testValidBSTOnlyRightChildren(self):
        # Tree: [1,null,3,null,5]
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testInvalidBSTLeftSubtreeViolation(self):
        # Tree: [10,5,15,null,null,6,20]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(20)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)

    def testValidBSTCompleteTree(self):
        # Tree: [8,3,10,1,6,null,14,null,null,4,7,13]
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right.right.left = TreeNode(13)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, True)

    def testInvalidBSTEqualToParent(self):
        # Tree: [1,1]
        root = TreeNode(1)
        root.left = TreeNode(1)
        result = self.solution.isValidBST(root)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()