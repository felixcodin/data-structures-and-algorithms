import unittest
from house_robber import Solution

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 2, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 4)

    def testAlternatingMax(self):
        nums = [2, 7, 9, 3, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 12)

    def testSingleHouse(self):
        nums = [5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 5)

    def testTwoHouses(self):
        nums = [1, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 2)

    def testTwoHousesEqual(self):
        nums = [2, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 2)

    def testAllSameValue(self):
        nums = [5, 5, 5, 5, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 15)

    def testIncreasingValues(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.rob(nums)
        self.assertEqual(result, 9)

    def testDecreasingValues(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 9)

    def testLargeGap(self):
        nums = [100, 1, 1, 100]
        result = self.solution.rob(nums)
        self.assertEqual(result, 200)

    def testConsecutiveSkip(self):
        nums = [2, 1, 1, 2]
        result = self.solution.rob(nums)
        self.assertEqual(result, 4)

    def testMaxAtStart(self):
        nums = [10, 1, 1, 1]
        result = self.solution.rob(nums)
        self.assertEqual(result, 11)

    def testMaxAtEnd(self):
        nums = [1, 1, 1, 10]
        result = self.solution.rob(nums)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()