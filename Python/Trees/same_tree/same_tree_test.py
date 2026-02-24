import unittest
from same_tree import Solution, TreeNode


class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBothNone(self):
        p = None
        q = None
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testFirstNoneSecondNot(self):
        p = None
        q = TreeNode(1)
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testFirstNotSecondNone(self):
        p = TreeNode(1)
        q = None
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testIdenticalSingleNode(self):
        p = TreeNode(1)
        q = TreeNode(1)
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testDifferentSingleNode(self):
        p = TreeNode(1)
        q = TreeNode(2)
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testLeetCodeExample1(self):
        # Tree: [1,2,3]
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        # p: [1,2], q: [1,null,2]
        p = TreeNode(1)
        p.left = TreeNode(2)
        
        q = TreeNode(1)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testLeetCodeExample3(self):
        # p: [1,2,1], q: [1,1,2]
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testIdenticalTwoLevels(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(4)
        p.left.right = TreeNode(5)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(4)
        q.left.right = TreeNode(5)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testDifferentStructureSameValues(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        
        q = TreeNode(1)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testSameStructureDifferentValues(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(3)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testLeftSkewedIdentical(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testRightSkewedIdentical(self):
        p = TreeNode(1)
        p.right = TreeNode(2)
        p.right.right = TreeNode(3)
        
        q = TreeNode(1)
        q.right = TreeNode(2)
        q.right.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testLeftSkewedDifferent(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(4)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testOneHasLeftChildOtherDoesNot(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        q = TreeNode(1)
        q.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testOneHasRightChildOtherDoesNot(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testCompleteBinaryTreeIdentical(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(4)
        p.left.right = TreeNode(5)
        p.right.left = TreeNode(6)
        p.right.right = TreeNode(7)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(4)
        q.left.right = TreeNode(5)
        q.right.left = TreeNode(6)
        q.right.right = TreeNode(7)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testMirrorTrees(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(3)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testDifferentDepth(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testOnlyLeftChildren(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        p.left.left.left = TreeNode(4)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(3)
        q.left.left.left = TreeNode(4)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testOnlyRightChildren(self):
        p = TreeNode(1)
        p.right = TreeNode(2)
        p.right.right = TreeNode(3)
        p.right.right.right = TreeNode(4)
        
        q = TreeNode(1)
        q.right = TreeNode(2)
        q.right.right = TreeNode(3)
        q.right.right.right = TreeNode(4)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testUnbalancedIdentical(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        p.right = TreeNode(4)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(3)
        q.right = TreeNode(4)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testSingleNodeWithChildren(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(2)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(2)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testNegativeValues(self):
        p = TreeNode(-1)
        p.left = TreeNode(-2)
        p.right = TreeNode(-3)
        
        q = TreeNode(-1)
        q.left = TreeNode(-2)
        q.right = TreeNode(-3)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testZeroValues(self):
        p = TreeNode(0)
        p.left = TreeNode(0)
        p.right = TreeNode(0)
        
        q = TreeNode(0)
        q.left = TreeNode(0)
        q.right = TreeNode(0)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testMixedPositiveNegative(self):
        p = TreeNode(1)
        p.left = TreeNode(-2)
        p.right = TreeNode(3)
        
        q = TreeNode(1)
        q.left = TreeNode(-2)
        q.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testLargeValues(self):
        p = TreeNode(100)
        p.left = TreeNode(200)
        p.right = TreeNode(300)
        
        q = TreeNode(100)
        q.left = TreeNode(200)
        q.right = TreeNode(300)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testDifferentAtLeaf(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(4)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(5)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testDifferentAtRoot(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        q = TreeNode(2)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testThreeLevelsIdentical(self):
        p = TreeNode(5)
        p.left = TreeNode(3)
        p.right = TreeNode(8)
        p.left.left = TreeNode(1)
        p.left.right = TreeNode(4)
        p.right.left = TreeNode(7)
        p.right.right = TreeNode(9)
        
        q = TreeNode(5)
        q.left = TreeNode(3)
        q.right = TreeNode(8)
        q.left.left = TreeNode(1)
        q.left.right = TreeNode(4)
        q.right.left = TreeNode(7)
        q.right.right = TreeNode(9)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testPartialTreeMismatch(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(4)
        
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.right.right = TreeNode(4)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testSymmetricValuesDifferentStructure(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        
        q = TreeNode(1)
        q.right = TreeNode(2)
        q.right.right = TreeNode(3)
        
        result = self.solution.isSameTree(p, q)
        self.assertFalse(result)

    def testBothSingleZero(self):
        p = TreeNode(0)
        q = TreeNode(0)
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)

    def testRepeatedValues(self):
        p = TreeNode(1)
        p.left = TreeNode(1)
        p.right = TreeNode(1)
        
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(1)
        
        result = self.solution.isSameTree(p, q)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()