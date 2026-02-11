import unittest
from maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [2, 3, -2, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def testWithTwoNegatives(self):
        nums = [-2, 0, -1]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 0)

    def testAllPositive(self):
        nums = [2, 3, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testAllNegative(self):
        nums = [-2, -3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 12)

    def testSinglePositive(self):
        nums = [5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 5)

    def testSingleNegative(self):
        nums = [-5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, -5)

    def testSingleZero(self):
        nums = [0]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 0)

    def testWithZeroInMiddle(self):
        nums = [2, 3, 0, 4, 5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 20)

    def testStartingWithZero(self):
        nums = [0, 2, 3, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testEndingWithZero(self):
        nums = [2, 3, 4, 0]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testMultipleZeros(self):
        nums = [0, 2, 0, 3, 0]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 3)

    def testAllZeros(self):
        nums = [0, 0, 0]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 0)

    def testTwoPositives(self):
        nums = [3, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 12)

    def testTwoNegatives(self):
        nums = [-3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 12)

    def testOnePositiveOneNegative(self):
        nums = [3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 3)

    def testOddNegatives(self):
        nums = [-2, 3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testEvenNegatives(self):
        nums = [-1, -2, -3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testLargeNumbers(self):
        nums = [1000, -1000, 1000]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 1000)

    def testComplexMixed(self):
        nums = [2, -5, -2, -4, 3]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def testNegativeAtEnd(self):
        nums = [2, 3, -1]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def testNegativeAtStart(self):
        nums = [-1, 2, 3]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def testZeroBreaksSequence(self):
        nums = [-2, -3, 0, -4, -5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 20)

    def testSmallNegativeProduct(self):
        nums = [0, -1, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 4)

    def testAlternatingSignsLong(self):
        nums = [-2, 3, -4, 2, -1, 5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 120)


if __name__ == '__main__':
    unittest.main()