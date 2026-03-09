import unittest
from unique_number_of_occurrences import Solution


class TestUniqueOccurrences(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicUniqueOccurrences(self):
        arr = [1, 2, 2, 1, 1, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testLeetCodeExample1(self):
        arr = [1, 2, 2, 1, 1, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        arr = [1, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testLeetCodeExample3(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testNonUniqueOccurrences(self):
        arr = [1, 1, 2, 2, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testSingleElement(self):
        arr = [1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoElementsSame(self):
        arr = [1, 1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoElementsDifferent(self):
        arr = [1, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testThreeElementsAllSame(self):
        arr = [5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testThreeElementsAllDifferent(self):
        arr = [1, 2, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testAllSameElement(self):
        arr = [7, 7, 7, 7, 7]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testUniqueOccurrences123(self):
        arr = [1, 2, 2, 3, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testDuplicateOccurrences(self):
        arr = [1, 1, 2, 2, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testNegativeNumbers(self):
        arr = [-1, -1, -2, -2, -2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testMixedPositiveNegative(self):
        arr = [-1, -1, 1, 1, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testWithZeros(self):
        arr = [0, 0, 1, 1, 1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testAllZeros(self):
        arr = [0, 0, 0, 0]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testFourDistinctOccurrences(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoSameOccurrences(self):
        arr = [1, 1, 1, 2, 2, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testLargeNumbers(self):
        arr = [1000, 1000, 2000, 2000, 2000]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testManyUniqueElements(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testOneOccurrenceEach(self):
        arr = [1, 2, 3, 4, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testDifferentOccurrenceCounts(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoGroups(self):
        arr = [1, 1, 2, 2, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testThreeGroups(self):
        arr = [1, 2, 2, 3, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testFourGroups(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testFiveGroups(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoGroupsSameCount(self):
        arr = [1, 1, 2, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testThreeGroupsSameCount(self):
        arr = [1, 1, 2, 2, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testAlternatingPattern(self):
        arr = [1, 2, 1, 2, 1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testConsecutiveNumbers(self):
        arr = [1, 2, 3, 4, 5, 6]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testRepeatedPairs(self):
        arr = [1, 1, 2, 2, 3, 3, 4, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testIncreasingOccurrences(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testDecreasingOccurrences(self):
        arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testRandomPattern(self):
        arr = [5, 5, 5, 7, 7, 9]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testLargeArray(self):
        arr = [1] * 10 + [2] * 20 + [3] * 30
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testLargeArrayDuplicate(self):
        arr = [1] * 10 + [2] * 10 + [3] * 20
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testMixedNegativePositiveZero(self):
        arr = [-1, -1, 0, 0, 0, 1, 1, 1, 1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSingleOccurrenceMultipleElements(self):
        arr = [10, 20, 30, 40, 50]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testTwoOccurrencesEach(self):
        arr = [1, 1, 2, 2, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testThreeOccurrencesEach(self):
        arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testMixedOccurrences12345(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testUnsortedArray(self):
        arr = [3, 1, 2, 3, 1, 2, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testUnsortedUniqueOccurrences(self):
        arr = [5, 1, 1, 2, 2, 2, 3, 3, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSparseValues(self):
        arr = [100, 200, 200, 300, 300, 300]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testNegativeAndPositive(self):
        arr = [-5, -5, 5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testManyDuplicates(self):
        arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testVeryLargeCount(self):
        arr = [1] * 100
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTwoElementsManyOccurrences(self):
        arr = [1] * 50 + [2] * 75
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testThreeElementsSameOccurrences(self):
        arr = [1] * 10 + [2] * 10 + [3] * 10
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testComplexPattern1(self):
        arr = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testComplexPattern2(self):
        arr = [7, 7, 8, 8, 9, 9]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testOnesAndTwos(self):
        arr = [1, 2, 2, 1, 1]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testFourElements(self):
        arr = [1, 2, 3, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testFiveElements(self):
        arr = [1, 2, 3, 4, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testSixElements(self):
        arr = [1, 1, 2, 2, 2, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSevenElements(self):
        arr = [1, 2, 2, 3, 3, 3, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testEightElements(self):
        arr = [1, 2, 2, 3, 3, 4, 4, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testNineElements(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testTenElements(self):
        arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testAllNegatives(self):
        arr = [-1, -1, -2, -2, -2, -3, -3, -3, -3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testMixedRange(self):
        arr = [-10, -10, 0, 0, 0, 10, 10, 10, 10]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSymmetricValues(self):
        arr = [-5, -5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testAsymmetricOccurrences(self):
        arr = [1, 1, 1, 2, 2, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testPowerOfTwo(self):
        arr = [1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testFibonacciPattern(self):
        arr = [1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testRepeatingDigits(self):
        arr = [11, 11, 22, 22, 22, 33, 33, 33, 33]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testScatteredPattern(self):
        arr = [5, 1, 5, 2, 5, 2, 3, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testMaxIntValue(self):
        arr = [2147483647, 2147483647, -2147483648, -2147483648, -2147483648]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testBoundaryValues(self):
        arr = [-1000, -1000, 0, 1000, 1000, 1000]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testMultipleSameOccurrences(self):
        arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testUniqueCountsVariety(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testNonSequentialNumbers(self):
        arr = [10, 10, 25, 25, 25, 50, 50, 50, 50]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSmallAndLargeNumbers(self):
        arr = [1, 1, 1000000, 1000000, 1000000, 1000000]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testRepeatedZeros(self):
        arr = [0, 0, 0, 1, 1, 2]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testMixedSequence(self):
        arr = [9, 8, 8, 7, 7, 7, 6, 6, 6, 6]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testDoubleDigits(self):
        arr = [10, 10, 20, 20, 30, 30]
        result = self.solution.uniqueOccurrences(arr)
        self.assertFalse(result)

    def testTripleDigits(self):
        arr = [100, 100, 200, 200, 200, 300, 300, 300, 300]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSinglePair(self):
        arr = [42, 42]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testSingleTriplet(self):
        arr = [99, 99, 99]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)

    def testComplexMix(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        result = self.solution.uniqueOccurrences(arr)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()