import unittest
from find_pivot_index import Solution


class TestPivotIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 7, 3, 6, 5, 6]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testLeetCodeExample1(self):
        nums = [1, 7, 3, 6, 5, 6]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testLeetCodeExample2(self):
        nums = [1, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testLeetCodeExample3(self):
        nums = [2, 1, -1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testNoPivot(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSingleElement(self):
        nums = [1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testSingleZero(self):
        nums = [0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testTwoElements(self):
        nums = [1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testTwoElementsPivotAtStart(self):
        nums = [0, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 1)

    def testTwoElementsPivotAtEnd(self):
        nums = [1, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testThreeElements(self):
        nums = [1, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 1)

    def testPivotAtStart(self):
        nums = [0, 1, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testPivotAtEnd(self):
        nums = [3, 2, 1, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testPivotInMiddle(self):
        nums = [1, 2, 3, 4, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testAllZeros(self):
        nums = [0, 0, 0, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testAllSamePositive(self):
        nums = [5, 5, 5, 5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testAllSameNegative(self):
        nums = [-5, -5, -5, -5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testWithNegativeNumbers(self):
        nums = [-1, -2, -3, -1, -1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testMixedPositiveNegative(self):
        nums = [1, -1, 2, -2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 4)

    def testZeroAtStart(self):
        nums = [0, 1, 2, 3, 4]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testZeroAtEnd(self):
        nums = [4, 3, 2, 1, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testZeroInMiddle(self):
        nums = [1, 2, 0, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testMultipleZeros(self):
        nums = [0, 0, 1, 0, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testLeftmostPivot(self):
        nums = [0, 5, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testRightmostPivot(self):
        nums = [3, 2, 5, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSymmetricArray(self):
        nums = [1, 2, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testAsymmetricArray(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testFourElements(self):
        nums = [1, 3, 2, 2]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testFiveElements(self):
        nums = [1, 2, 3, 4, 10]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSixElements(self):
        nums = [1, 2, 3, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSevenElements(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testLargeNumbers(self):
        nums = [100, 200, 300, 400, 500]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSmallNumbers(self):
        nums = [1, 1, 1, 1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testNegativeAtStart(self):
        nums = [-7, 1, 5, 2, -4, 3, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testNegativeAtEnd(self):
        nums = [1, 2, 3, 4, -10]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testAllNegative(self):
        nums = [-1, -2, -3, -4, -5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testZeroSumArray(self):
        nums = [1, -1, 2, -2, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 4)

    def testPositiveSumArray(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testNegativeSumArray(self):
        nums = [-1, -2, -3, -4, -5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testPivotWithLargeLeft(self):
        nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testPivotWithLargeRight(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testConsecutiveNumbers(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testReversedConsecutive(self):
        nums = [6, 5, 4, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testAlternatingValues(self):
        nums = [1, -1, 1, -1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testEightElements(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 5)

    def testNineElements(self):
        nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 4)

    def testTenElements(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testBalancedAtSecondPosition(self):
        nums = [1, 7, 3, 6, 5, 6]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testNoBalancePoint(self):
        nums = [1, 3, 5, 7, 9]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testWithDuplicates(self):
        nums = [1, 1, 1, 3, 1, 1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testLargePivotValue(self):
        nums = [1, 1, 100, 1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testSmallPivotValue(self):
        nums = [10, 10, 1, 10, 10]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testPivotEqualsZero(self):
        nums = [1, 2, 0, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testMultiplePossiblePivotsReturnsFirst(self):
        nums = [0, 0, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testLeftSideEmpty(self):
        nums = [0, 5, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testRightSideEmpty(self):
        nums = [3, 2, 5, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testBothSidesEmpty(self):
        nums = [42]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testComplexPattern(self):
        nums = [1, 3, 2, 4, 1, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 3)

    def testVeryLargeArray(self):
        nums = [1] * 100 + [100] + [1] * 100
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 100)

    def testMixedPattern(self):
        nums = [5, -3, 2, 4, -6, 8]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 4)

    def testAllPositiveNoPivot(self):
        nums = [2, 4, 6, 8, 10]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testIncreasingSequence(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testDecreasingSequence(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testMountainPattern(self):
        nums = [1, 2, 3, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testValleyPattern(self):
        nums = [3, 2, 1, 2, 3]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testZerosAroundPivot(self):
        nums = [0, 0, 5, 0, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testNegativesAroundZero(self):
        nums = [-1, -2, 0, -2, -1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testLargeLeftSmallRight(self):
        nums = [100, 1, 1, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testSmallLeftLargeRight(self):
        nums = [1, 1, 1, 100]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testBalancedEvenLength(self):
        nums = [1, 2, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)

    def testBalancedOddLength(self):
        nums = [1, 2, 0, 2, 1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testFirstElementIsPivot(self):
        nums = [0, 1, -1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 0)

    def testLastElementIsPivot(self):
        nums = [1, -1, 0]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, 2)

    def testMiddleElementIsPivot(self):
        nums = [1, 0, -1]
        result = self.solution.pivotIndex(nums)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()