import unittest
from kth_smallest_element_in_a_bst import Solution, TreeNode

class TestKthSmallestElementInBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleNode(self):
        root = TreeNode(1)
        result = self.solution.kthSmallest(root, 1)
        self.assertEqual(result, 1)

    def testTwoNodesKFirst(self):
        # BST: [1,null,2]
        root = TreeNode(1)
        root.right = TreeNode(2)
        result = self.solution.kthSmallest(root, 1)
        self.assertEqual(result, 1)

    def testTwoNodesKSecond(self):
        # BST: [1,null,2]
        root = TreeNode(1)
        root.right = TreeNode(2)
        result = self.solution.kthSmallest(root, 2)
        self.assertEqual(result, 2)

    def testThreeNodesKMiddle(self):
        # BST: [2,1,3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        result = self.solution.kthSmallest(root, 2)
        self.assertEqual(result, 2)

    def testComplexBSTKFirst(self):
        # BST: [3,1,4,null,2]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        result = self.solution.kthSmallest(root, 1)
        self.assertEqual(result, 1)

    def testComplexBSTKThird(self):
        # BST: [5,3,6,2,4,null,null,1]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        result = self.solution.kthSmallest(root, 3)
        self.assertEqual(result, 3)

    def testLargerBSTKLast(self):
        # BST: [5,3,6,2,4,null,null,1]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        result = self.solution.kthSmallest(root, 6)
        self.assertEqual(result, 6)

    def testRightSkewedBST(self):
        # BST: [1,null,2,null,3,null,4]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        result = self.solution.kthSmallest(root, 3)
        self.assertEqual(result, 3)

    def testLeftSkewedBST(self):
        # BST: [4,3,null,2,null,1]
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        result = self.solution.kthSmallest(root, 2)
        self.assertEqual(result, 2)

    def testBalancedBSTKMiddle(self):
        # BST: [4,2,6,1,3,5,7]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        result = self.solution.kthSmallest(root, 4)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()