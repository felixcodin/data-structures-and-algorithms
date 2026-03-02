import unittest
from maximum_average_subarray_i import Solution


class TestFindMaxAverage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 12.75)

    def testLeetCodeExample1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 12.75)

    def testLeetCodeExample2(self):
        nums = [5]
        k = 1
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testSingleElement(self):
        nums = [10]
        k = 1
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 10.0)

    def testArraySizeEqualsK(self):
        nums = [1, 2, 3, 4, 5]
        k = 5
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 3.0)

    def testTwoElements(self):
        nums = [3, 7]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testKEqualsOne(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testAllPositive(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testAllNegative(self):
        nums = [-1, -2, -3, -4, -5]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, -1.5)

    def testMixedPositiveNegative(self):
        nums = [-1, 5, -3, 7, 2]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 3.0, places=5)

    def testWithZeros(self):
        nums = [0, 0, 0, 1, 2]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 1.0)

    def testAllZeros(self):
        nums = [0, 0, 0, 0]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 0.0)

    def testAllSameElements(self):
        nums = [5, 5, 5, 5, 5]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testMaxAtStart(self):
        nums = [10, 9, 8, 1, 2, 3]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 9.0)

    def testMaxAtEnd(self):
        nums = [1, 2, 3, 8, 9, 10]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 9.0)

    def testMaxInMiddle(self):
        nums = [1, 2, 10, 9, 8, 1, 2]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 9.0)

    def testDecreasingArray(self):
        nums = [10, 9, 8, 7, 6, 5]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 9.5)

    def testIncreasingArray(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.5)

    def testWithDuplicates(self):
        nums = [1, 1, 5, 5, 3, 3]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testLargeK(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 8
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 6.5)

    def testSmallK(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 9.5)

    def testNegativeAtStart(self):
        nums = [-5, -4, 10, 11, 12]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 11.0)

    def testNegativeAtEnd(self):
        nums = [10, 11, 12, -4, -5]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 11.0)

    def testAlternatingValues(self):
        nums = [1, -1, 1, -1, 1, -1]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 0.0)

    def testLargerNumbers(self):
        nums = [100, 200, 300, 400, 500]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 400.0)

    def testNegativeLargerNumbers(self):
        nums = [-100, -200, -300, -400, -500]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, -200.0)

    def testThreeElements(self):
        nums = [1, 2, 3]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 2.5)

    def testFourElements(self):
        nums = [1, 2, 3, 4]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 3.5)

    def testKEquals3(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 6.0)

    def testKEquals4(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 4
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 6.5)

    def testConsecutiveNumbers(self):
        nums = [5, 6, 7, 8, 9]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 8.0)

    def testZeroInMiddle(self):
        nums = [10, 5, 0, 5, 10]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.0)

    def testSingleNegative(self):
        nums = [-1]
        k = 1
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, -1.0)

    def testLongArray(self):
        nums = list(range(1, 21))
        k = 5
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 18.0)

    def testRepeatingPattern(self):
        nums = [1, 2, 1, 2, 1, 2]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 1.5)

    def testLargeVariance(self):
        nums = [1, 100, 1, 100, 1]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 50.5)

    def testSmallVariance(self):
        nums = [5, 5, 6, 6, 5, 5]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 6.0)

    def testMixedZeros(self):
        nums = [0, 1, 0, 1, 0]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 0.5)

    def testNegativeZeroPositive(self):
        nums = [-1, 0, 1, 2, 3]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 2.0)

    def testIntegerDivision(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 4.5)

    def testPerfectAverage(self):
        nums = [6, 6, 6, 6]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 6.0)

    def testFractionResult(self):
        nums = [1, 2, 3]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 2.5)

    def testLargeArraySmallK(self):
        nums = list(range(1, 101))
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 99.0)

    def testLargeArrayLargeK(self):
        nums = list(range(1, 101))
        k = 50
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 75.5)

    def testAlternatingHighLow(self):
        nums = [10, 1, 10, 1, 10, 1]
        k = 2
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 5.5)

    def testSuddenDrop(self):
        nums = [10, 10, 10, 1, 1, 1]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 10.0)

    def testSuddenRise(self):
        nums = [1, 1, 1, 10, 10, 10]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 10.0)

    def testMiddlePeak(self):
        nums = [1, 2, 10, 2, 1]
        k = 3
        result = self.solution.findMaxAverage(nums, k)
        self.assertAlmostEqual(result, 4.666666666666667, places=5)


if __name__ == '__main__':
    unittest.main()