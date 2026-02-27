import unittest
from increasing_triplet_subsequence import Solution


class TestIncreasingTriplet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicTriplet(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testLeetCodeExample1(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testLeetCodeExample3(self):
        nums = [2, 1, 5, 0, 4, 6]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testNoTriplet(self):
        nums = [5, 4, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testTwoElements(self):
        nums = [1, 2]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testOneElement(self):
        nums = [1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testEmptyArray(self):
        nums = []
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testThreeElementsIncreasing(self):
        nums = [1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testThreeElementsDecreasing(self):
        nums = [3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testThreeElementsNotIncreasing(self):
        nums = [1, 3, 2]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testTripletAtStart(self):
        nums = [1, 2, 3, 0, 0, 0]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testTripletAtEnd(self):
        nums = [5, 5, 5, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testTripletInMiddle(self):
        nums = [5, 1, 2, 3, 0]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testAllSameElements(self):
        nums = [1, 1, 1, 1, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testWithDuplicates(self):
        nums = [1, 1, 2, 2, 3, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testDuplicatesNoTriplet(self):
        nums = [3, 3, 2, 2, 1, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testNegativeNumbers(self):
        nums = [-3, -2, -1]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testMixedPositiveNegative(self):
        nums = [-1, 0, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testNegativeNoTriplet(self):
        nums = [-1, -2, -3]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testLargeGap(self):
        nums = [1, 100, 200]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testSmallGap(self):
        nums = [1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testZigZagPattern(self):
        nums = [1, 3, 2, 4, 3, 5]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testAlternatingHighLow(self):
        nums = [10, 1, 9, 2, 8, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testLongDecreasing(self):
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testLongIncreasing(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testTripletNotConsecutive(self):
        nums = [1, 5, 0, 2, 0, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testResetFirst(self):
        nums = [5, 1, 2, 6]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testResetFirstAndSecond(self):
        nums = [9, 8, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testFourElements(self):
        nums = [1, 2, 3, 4]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testFourElementsNoTriplet(self):
        nums = [4, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testComplexPattern(self):
        nums = [20, 100, 10, 12, 5, 13]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testAlmostTriplet(self):
        nums = [1, 5, 2]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testTwoIncreasingPairs(self):
        nums = [1, 2, 10, 11]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testMultiplePotentialTriplets(self):
        nums = [1, 2, 3, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testLargeNumbers(self):
        nums = [1000, 2000, 3000]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testZeroValues(self):
        nums = [-1, 0, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testAllZeros(self):
        nums = [0, 0, 0]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testMinMaxValues(self):
        nums = [-2147483648, 0, 2147483647]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testPlateau(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testVShaped(self):
        nums = [5, 4, 3, 4, 5]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testInvertedVShaped(self):
        nums = [1, 2, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testSinglePeak(self):
        nums = [1, 5, 2]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testSingleValley(self):
        nums = [5, 1, 4]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testStrictlyIncreasingStart(self):
        nums = [1, 2, 3, 2, 1, 0]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testStrictlyDecreasingEnd(self):
        nums = [5, 4, 3, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testManySmallNumbers(self):
        nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testDescendingThenAscending(self):
        nums = [5, 4, 3, 2, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testAscendingThenDescending(self):
        nums = [1, 2, 3, 4, 3, 2, 1]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testLongArrayNoTriplet(self):
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        result = self.solution.increasingTriplet(nums)
        self.assertFalse(result)

    def testTripletWithRepeatedMin(self):
        nums = [1, 1, 2, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testTripletWithRepeatedMax(self):
        nums = [1, 2, 3, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testEdgeCase1(self):
        nums = [1, 0, 2, 0, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)

    def testEdgeCase2(self):
        nums = [1, 5, 0, 4, 1, 3]
        result = self.solution.increasingTriplet(nums)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()