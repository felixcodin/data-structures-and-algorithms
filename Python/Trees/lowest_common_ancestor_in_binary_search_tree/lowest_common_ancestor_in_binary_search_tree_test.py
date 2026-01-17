import unittest
from lowest_common_ancestor_in_binary_search_tree import Solution, TreeNode

class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        # Tree: [6,2,8,0,4,7,9,null,null,3,5]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        
        p = root.left  # 2
        q = root.right  # 8
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 6)

    def testBothInLeftSubtree(self):
        # Tree: [6,2,8,0,4,7,9,null,null,3,5]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        
        p = root.left  # 2
        q = root.left.right  # 4
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def testBothInRightSubtree(self):
        # Tree: [6,2,8,7,9]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        
        p = root.right.left  # 7
        q = root.right.right  # 9
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 8)

    def testOneNodeIsAncestor(self):
        # Tree: [6,2,8,0,4]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        
        p = root.left  # 2
        q = root.left.left  # 0
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def testRootIsLCA(self):
        # Tree: [2,1,3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        p = root.left  # 1
        q = root.right  # 3
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def testTwoNodes(self):
        # Tree: [2,1]
        root = TreeNode(2)
        root.left = TreeNode(1)
        
        p = root  # 2
        q = root.left  # 1
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def testSameNode(self):
        # Tree: [6,2,8,0,4]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        
        p = root.left  # 2
        q = root.left  # 2
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

    def testDeepTree(self):
        # Tree: [10,5,15,3,7,13,18,1,4]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left.left = TreeNode(1)
        root.left.left.right = TreeNode(4)
        
        p = root.left.left.left  # 1
        q = root.left.right  # 7
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 5)


if __name__ == '__main__':
    unittest.main()