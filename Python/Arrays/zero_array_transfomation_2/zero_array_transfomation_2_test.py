import unittest
from zero_array_transfomation_2 import Solution

class TestMinZeroArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [2,0,2]
        queries = [[0,2,1], [0,2,1], [1,2,2]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, 2)

    def testNoPossibleZeroArray(self):
        nums = [4,3,2,1]
        queries = [[1, 3, 2], [0, 2, 1]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, -1)

    def testSingleQuerySufficient(self):
        nums = [5,5,5]
        queries = [[0, 2, 5], [0, 1, 3], [1, 2, 2]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, 1)

    def testLargeValuesWithMultipleQueries(self):
        nums = [10, 20, 30, 40, 50]
        queries = [[0, 4, 10], [1, 3, 15], [2, 2, 5], [0, 0, 5], [4, 4, 50]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, -1)

    def testEdgeCaseWithNoQueries(self):
        nums = [1,2,3]
        queries = []
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, -1)

    def testLargeArrayWithUniformValues(self):
        nums = [100000] * 100000
        queries = [[0, 99999, 100000]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, 1)

    def testIncrementalQueries(self):
        nums = [3,3,3]
        queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [0, 2, 2]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, 4)

    def testMinimalArray(self):
        nums = [1]
        queries = [[0,0,1]]
        res = self.solution.minZeroArray(nums, queries)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()