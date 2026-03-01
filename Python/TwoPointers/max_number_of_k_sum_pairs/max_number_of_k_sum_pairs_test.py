import unittest
from max_number_of_k_sum_pairs import Solution


class TestMaxOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 2, 3, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testLeetCodeExample1(self):
        nums = [1, 2, 3, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testLeetCodeExample2(self):
        nums = [3, 1, 3, 4, 3]
        k = 6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testNoPairs(self):
        nums = [1, 2, 3, 4]
        k = 10
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testEmptyArray(self):
        nums = []
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testSingleElement(self):
        nums = [5]
        k = 10
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testTwoElementsMatch(self):
        nums = [2, 3]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testTwoElementsNoMatch(self):
        nums = [1, 2]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testAllSameElements(self):
        nums = [2, 2, 2, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testAllSameElementsOddCount(self):
        nums = [2, 2, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testDuplicates(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testMultiplePairs(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 7
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testNegativeNumbers(self):
        nums = [-1, -2, 3, 4]
        k = 2
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testAllNegative(self):
        nums = [-5, -3, -2, -1]
        k = -4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testWithZeros(self):
        nums = [0, 0, 1, 1]
        k = 1
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testAllZeros(self):
        nums = [0, 0, 0, 0]
        k = 0
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testKIsZero(self):
        nums = [-1, 0, 1, 2]
        k = 0
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testLargeNumbers(self):
        nums = [1000, 2000, 3000, 4000]
        k = 5000
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testKLargerThanAllElements(self):
        nums = [1, 2, 3, 4]
        k = 100
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testKSmallerThanAllElements(self):
        nums = [10, 20, 30, 40]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testOnePair(self):
        nums = [1, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testThreeElements(self):
        nums = [1, 2, 3]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testFourElementsTwoPairs(self):
        nums = [1, 3, 2, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testUnsortedArray(self):
        nums = [4, 1, 3, 2, 5, 6]
        k = 7
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testDuplicatePairs(self):
        nums = [2, 2, 2, 2, 2, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testMixedPositiveNegative(self):
        nums = [-5, 5, -3, 3, -1, 1]
        k = 0
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testOddNumberOfElements(self):
        nums = [1, 2, 3, 4, 5]
        k = 6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testEvenNumberOfElements(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 7
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testConsecutiveNumbers(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 9
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 4)

    def testNoValidPairsDueTok(self):
        nums = [1, 1, 1, 1]
        k = 3
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testHalfElementsFormPairs(self):
        nums = [1, 4, 2, 3, 5, 5]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testLargeArray(self):
        nums = list(range(1, 101))
        k = 101
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 50)

    def testRepeatedSmallNumbers(self):
        nums = [1, 1, 1, 1, 2, 2, 2, 2]
        k = 3
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 4)

    def testSinglePairPossible(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testElementEqualToK(self):
        nums = [5, 5, 5, 5]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testHalfK(self):
        nums = [3, 3, 3, 3]
        k = 6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testMixedDuplicates(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 4)

    def testOnlyOnePairExists(self):
        nums = [1, 9, 2, 8, 3, 7, 4, 6]
        k = 10
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 4)

    def testMaxPairsWithDuplicates(self):
        nums = [1, 1, 1, 4, 4, 4]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testAsymmetricPairs(self):
        nums = [1, 1, 1, 5]
        k = 6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)

    def testNegativeK(self):
        nums = [-5, -4, -3, -2, -1]
        k = -6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testZeroAndNegative(self):
        nums = [0, -1, 1, -2, 2]
        k = 0
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testAllElementsTooLarge(self):
        nums = [10, 20, 30]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testAllElementsTooSmall(self):
        nums = [1, 2, 3]
        k = 100
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)

    def testComplexPattern(self):
        nums = [3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testTwoOfEach(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 3)

    def testKEqualsOne(self):
        nums = [0, 1, 0, 1]
        k = 1
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testKEqualsTwo(self):
        nums = [1, 1, 1, 1]
        k = 2
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)

    def testLongerSequence(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 11
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 5)

    def testManyDuplicates(self):
        nums = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()