import unittest
from products_of_array_except_self import Solution

class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [1, 2, 3, 4]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [24, 12, 8, 6])

    def testArrayWithAZero(self):
        nums = [1, 2, 0, 4]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [0, 0, 8, 0])

    def testArrayWithMultipleZeros(self):
        nums = [0, 0, 0, 0]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [0, 0, 0, 0])

    def testArrayWithNegativeNumbers(self):
        nums = [-1, -2, -3, -4]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [-24, -12, -8, -6])

    def testArrayWithBothPositiveAndNegativeNumbers(self):
        nums = [-1, 2, -3, 4]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [-24, 12, -8, 6])

    def testSingleElementArray(self):
        nums = [5]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [1])

    def testTwoElementsArray(self):
        nums = [3, 4]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [4, 3])

    def testArrayWithAllOnes(self):
        nums = [1, 1, 1, 1]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [1, 1, 1, 1])

    def testArrayWithLargeNumbers(self):
        nums = [1000, 2000, 3000, 4000]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [24000000000, 12000000000, 8000000000, 6000000000])

    def testArrayWithMixed(self):
        nums = [1, -1, 0, 3, -3]
        res = self.solution.productExceptSelf(nums)
        self.assertEqual(res, [0, 0, 9, 0, 0])

if __name__ == '__main__':
    unittest.main()