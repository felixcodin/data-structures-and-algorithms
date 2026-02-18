import unittest
from convert_sorted_array_to_binary_search_tree import Solution, TreeNode


class TestConvertSortedArrayToBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def is_valid_bst(self, root, min_val=float('-inf'), max_val=float('inf')):
        """Helper function to validate BST property"""
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return (self.is_valid_bst(root.left, min_val, root.val) and
                self.is_valid_bst(root.right, root.val, max_val))

    def get_height(self, root):
        """Helper function to get tree height"""
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def is_balanced(self, root):
        """Helper function to check if tree is height-balanced"""
        if not root:
            return True
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def inorder_traversal(self, root):
        """Helper function to get inorder traversal"""
        if not root:
            return []
        return (self.inorder_traversal(root.left) + 
                [root.val] + 
                self.inorder_traversal(root.right))

    def testLeetCodeExample1(self):
        nums = [-10, -3, 0, 5, 9]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)
        self.assertEqual(result.val, 0)

    def testLeetCodeExample2(self):
        nums = [1, 3]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testSingleElement(self):
        nums = [1]
        result = self.solution.sortedArrayToBST(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))

    def testTwoElements(self):
        nums = [1, 2]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testThreeElements(self):
        nums = [1, 2, 3]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 2)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testOddLengthArray(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 4)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testEvenLengthArray(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testAllNegativeNumbers(self):
        nums = [-10, -5, -3, -1]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testAllPositiveNumbers(self):
        nums = [1, 3, 5, 7, 9, 11]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testMixedNumbers(self):
        nums = [-5, -2, 0, 3, 8, 12]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testConsecutiveNumbers(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testLargerArray(self):
        nums = list(range(-20, 21))
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testDuplicatesNotAllowed(self):
        # The problem assumes distinct values, but testing sorted array behavior
        nums = [1, 5, 10, 15, 20]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testTreeHeight(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        result = self.solution.sortedArrayToBST(nums)
        height = self.get_height(result)
        # For 15 elements, height should be 4 (log2(15) ≈ 3.9)
        self.assertTrue(height <= 5)
        self.assertTrue(self.is_balanced(result))

    def testZeroIncluded(self):
        nums = [-3, -1, 0, 1, 3]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 0)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))

    def testPowerOfTwoLength(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        height = self.get_height(result)
        self.assertEqual(height, 4)

    def testNonConsecutiveNumbers(self):
        nums = [2, 5, 11, 15, 20, 27]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)

    def testLargeNegativeToPositive(self):
        nums = [-100, -50, 0, 50, 100]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 0)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))

    def testFourElements(self):
        nums = [1, 2, 3, 4]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(self.is_valid_bst(result))
        self.assertTrue(self.is_balanced(result))
        self.assertEqual(self.inorder_traversal(result), nums)


if __name__ == '__main__':
    unittest.main()