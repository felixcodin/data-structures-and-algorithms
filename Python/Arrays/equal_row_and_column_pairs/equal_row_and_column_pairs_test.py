import unittest
from equal_row_and_column_pairs import Solution


class TestEqualPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 1)

    def testLeetCodeExample1(self):
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 1)

    def testLeetCodeExample2(self):
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testSingleElement(self):
        grid = [[1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 1)

    def testTwoByTwoMatching(self):
        grid = [[1, 2], [1, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTwoByTwoNoMatch(self):
        grid = [[1, 2], [3, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTwoByTwoIdentity(self):
        grid = [[1, 0], [0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 2)

    def testAllSameElements(self):
        grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testNoMatchingPairs(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testAllMatchingPairs(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testSymmetricGrid(self):
        grid = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testDiagonalMatch(self):
        grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testDuplicateRows(self):
        grid = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testDuplicateColumns(self):
        grid = [[1, 1, 4], [2, 2, 5], [3, 3, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testDuplicateRowsAndMatchingColumn(self):
        grid = [[1, 2], [1, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testThreeByThreeOneMatch(self):
        grid = [[1, 2, 3], [4, 5, 6], [1, 4, 7]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testThreeByThreeTwoMatches(self):
        grid = [[1, 2, 3], [2, 5, 8], [3, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testFourByFour(self):
        grid = [[1, 2, 3, 4], [2, 5, 6, 7], [3, 6, 8, 9], [4, 7, 9, 10]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testWithNegativeNumbers(self):
        grid = [[-1, -2, -3], [-2, -5, -6], [-3, -6, -9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testWithZeros(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testMixedZerosAndOnes(self):
        grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testWithNegativesAndPositives(self):
        grid = [[1, -1, 2], [-1, 3, -2], [2, -2, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testLargeNumbers(self):
        grid = [[1000, 2000, 3000], [2000, 5000, 6000], [3000, 6000, 9000]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testTwoByTwoAllDifferent(self):
        grid = [[1, 2], [3, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTwoByTwoPartialMatch(self):
        grid = [[1, 2], [2, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 2)

    def testThreeByThreeNoMatch(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testFourByFourNoMatch(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testFiveByFive(self):
        grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testMultipleDuplicateRows(self):
        grid = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testMultipleDuplicateRowsAndColumn(self):
        grid = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTwoDuplicateRows(self):
        grid = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTwoDuplicateRowsOneMatch(self):
        grid = [[1, 2, 3], [1, 2, 3], [1, 1, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testTransposedGrid(self):
        grid = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testAntiDiagonal(self):
        grid = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testSingleRowColumnMatch(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testRowMatchesItselfAsColumn(self):
        grid = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testThreeMatchingPairs(self):
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testAlternatingPattern(self):
        grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testIncreasingNumbers(self):
        grid = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testDecreasingNumbers(self):
        grid = [[5, 4, 3], [4, 3, 2], [3, 2, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testCheckerboard(self):
        grid = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 8)

    def testSparseMatrix(self):
        grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testDenseMatrix(self):
        grid = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testTwoMatchesInFourByFour(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 5, 9, 13], [2, 6, 10, 14]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testThreeMatchesInThreeByThree(self):
        grid = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testFourMatchesInFourByFour(self):
        grid = [[1, 2, 3, 4], [2, 5, 6, 7], [3, 6, 8, 9], [4, 7, 9, 10]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testRandomPattern1(self):
        grid = [[11, 1], [1, 11]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 2)

    def testRandomPattern2(self):
        grid = [[13, 13], [13, 13]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testMixedPositiveNegative(self):
        grid = [[1, -1, 2], [-1, 1, -2], [2, -2, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testPalindromeRow(self):
        grid = [[1, 2, 1], [2, 5, 2], [1, 2, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testSequentialNumbers(self):
        grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testReverseSequential(self):
        grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testComplexPattern1(self):
        grid = [[10, 20, 30], [20, 40, 60], [30, 60, 90]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testComplexPattern2(self):
        grid = [[7, 14, 21], [14, 28, 42], [21, 42, 63]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testBoundaryValues(self):
        grid = [[0, 1000000], [1000000, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 2)

    def testRepeatedValues1(self):
        grid = [[2, 2], [2, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testRepeatedValues2(self):
        grid = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testSingleDifferentElement(self):
        grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testCornerElements(self):
        grid = [[1, 0, 2], [0, 0, 0], [3, 0, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 1)

    def testXPattern(self):
        grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testPlusPattern(self):
        grid = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testFramePattern(self):
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testHollowCenter(self):
        grid = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 8)

    def testDiagonalOnes(self):
        grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testAllOnesExceptDiagonal(self):
        grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testUpperTriangular(self):
        grid = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testLowerTriangular(self):
        grid = [[1, 0, 0], [2, 3, 0], [4, 5, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testFiveByFiveIdentity(self):
        grid = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testScalarMultiple(self):
        grid = [[2, 4, 6], [4, 8, 12], [6, 12, 18]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testRowOfZeros(self):
        grid = [[0, 0, 0], [1, 2, 3], [4, 5, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testColumnOfZeros(self):
        grid = [[0, 1, 4], [0, 2, 5], [0, 3, 6]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testMixedSequence(self):
        grid = [[5, 10, 15], [10, 20, 30], [15, 30, 45]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testAsymmetricValues(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testSymmetricTwoByTwo(self):
        grid = [[1, 2], [2, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 2)

    def testPerfectSquares(self):
        grid = [[1, 4, 9], [4, 16, 36], [9, 36, 81]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testPrimeNumbers(self):
        grid = [[2, 3, 5], [3, 5, 7], [5, 7, 11]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testFibonacciNumbers(self):
        grid = [[1, 1, 2], [1, 2, 3], [2, 3, 5]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testPowersOfTwo(self):
        grid = [[1, 2, 4], [2, 4, 8], [4, 8, 16]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testNegativeDiagonal(self):
        grid = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testAlternatingNegatives(self):
        grid = [[1, -1, 1], [-1, 1, -1], [1, -1, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testLargeEqualGrid(self):
        grid = [[100] * 3 for _ in range(3)]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 9)

    def testMixedLargeSmall(self):
        grid = [[1000, 1, 1000], [1, 1, 1], [1000, 1, 1000]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 5)

    def testComplexFourByFour(self):
        grid = [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testMagicSquare(self):
        grid = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testConsecutivePairs(self):
        grid = [[1, 2], [3, 4]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testReversedRows(self):
        grid = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 0)

    def testShiftedRows(self):
        grid = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 3)

    def testCyclicPattern(self):
        grid = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 4)

    def testLastExample(self):
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        result = self.solution.equalPairs(grid)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()