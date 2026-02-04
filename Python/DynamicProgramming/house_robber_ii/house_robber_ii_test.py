import unittest
from house_robber_ii import Solution

class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleHouse(self):
        nums = [1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 1)

    def testTwoHouses(self):
        nums = [1, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 2)

    def testThreeHouses(self):
        nums = [2, 3, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 3)

    def testBasicCase(self):
        nums = [1, 2, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 4)

    def testLargerCase(self):
        nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 16)

    def testAllSameValue(self):
        nums = [5, 5, 5, 5, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 10)

    def testIncreasingValues(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 8)

    def testDecreasingValues(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 8)

    def testLargeFirstAndLast(self):
        nums = [100, 1, 1, 1, 100]
        result = self.solution.rob(nums)
        self.assertEqual(result, 101)

    def testAlternatingHighLow(self):
        nums = [10, 1, 10, 1, 10]
        result = self.solution.rob(nums)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()