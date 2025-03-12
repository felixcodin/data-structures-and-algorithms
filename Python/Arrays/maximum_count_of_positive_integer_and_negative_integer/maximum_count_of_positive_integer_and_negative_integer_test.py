import unittest
from maximum_count_of_positive_integer_and_negative_integer import Solution

class TestCountMaximum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [-2,-1,-1,1,2,3]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 3)

    def testAllPositvieNumber(self):
        nums = [1,2,3,4,5]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 5)

    def testAllNegativeNumber(self):
        nums = [-4,-3,-2,-1]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 4)

    def testMixedPositiveAndNegativeInteger(self):
        nums = [-2,-1,4,5,6,7]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 4)

    def testContainZero(self):
        nums = [0,1,2,3,4,5,6,7]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 7)

    def testSinglePositiveNumber(self):
        nums = [10]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 1)

    def testSingleNegativeNumber(self):
        nums = [-99]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 1)

    def testListWithRepeatValue(self):
        nums = [-1,-1,1,1,1,3,3]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 5)
    
    def testLargeNumber(self):
        nums = [-3000000, -2000000, -1000000, 1000000, 2000000, 3000000]
        res = self.solution.maximumCount(nums)
        self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()
