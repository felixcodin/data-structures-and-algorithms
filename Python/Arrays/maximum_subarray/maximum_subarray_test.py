import unittest
from maximum_subarray import Solution

class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testExampleCase(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        res = self.solution.maximumSubarray(nums)
        self.assertEqual(res, 6)

    def testSingleElement(self):
        nums = [1]
        res = self.solution.maximumSubarray(nums)
        self.assertEqual(res, 1)

    def testAllNegative(self):
        nums = [-1, -2, -3, -4]
        res = self.solution.maximumSubarray(nums)
        self.assertEqual(res, -1)

    def testMixedPositiveAndNegative(self):
        nums = [5, 4, -1, 7, 8]
        res = self.solution.maximumSubarray(nums)
        self.assertEqual(res, 23)

    def testAllPositive(self):
        nums = [1, 2, 3, 4, 5]
        res = self.solution.maximumSubarray(nums)
        self.assertEqual(res, 15)

if __name__ == '__main__':
    unittest.main()
