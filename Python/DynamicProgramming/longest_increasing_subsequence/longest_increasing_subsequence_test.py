import unittest
from longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicIncreasing(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def testAllIncreasing(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 5)

    def testAllDecreasing(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def testAllSame(self):
        nums = [7, 7, 7, 7, 7]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def testSingleElement(self):
        nums = [1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def testTwoElementsIncreasing(self):
        nums = [1, 3]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 2)

    def testTwoElementsDecreasing(self):
        nums = [3, 1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def testWithDuplicates(self):
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 6)

    def testLongSequence(self):
        nums = [0, 1, 0, 3, 2, 3]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def testWithNegatives(self):
        nums = [-2, -1, 0, 1, 2]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 5)

    def testMixedNegativesPositives(self):
        nums = [-10, 9, -5, 2, 5, 3, 7, 101, 18]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 6)

    def testAlternatingPattern(self):
        nums = [1, 5, 2, 6, 3, 7]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def testLargeNumbers(self):
        nums = [1000, 2000, 500, 3000, 1500, 4000]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def testComplexCase(self):
        nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()