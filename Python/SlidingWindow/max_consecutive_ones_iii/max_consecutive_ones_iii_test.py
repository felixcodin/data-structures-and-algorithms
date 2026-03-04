import unittest
from max_consecutive_ones_iii import Solution


class TestLongestOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testLeetCodeExample1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testLeetCodeExample2(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 10)

    def testKEqualsZero(self):
        nums = [1, 1, 0, 1, 1, 1, 0, 1]
        k = 0
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testKEqualsZeroAllOnes(self):
        nums = [1, 1, 1, 1, 1]
        k = 0
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testKEqualsZeroAllZeros(self):
        nums = [0, 0, 0, 0]
        k = 0
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 0)

    def testAllOnes(self):
        nums = [1, 1, 1, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testAllZeros(self):
        nums = [0, 0, 0, 0, 0]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testAllZerosKLarge(self):
        nums = [0, 0, 0, 0, 0]
        k = 10
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testSingleElementOne(self):
        nums = [1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 1)

    def testSingleElementZero(self):
        nums = [0]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 1)

    def testSingleElementZeroKZero(self):
        nums = [0]
        k = 0
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 0)

    def testTwoElements(self):
        nums = [1, 0]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 2)

    def testTwoElementsKZero(self):
        nums = [1, 0]
        k = 0
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 1)

    def testKEqualsOne(self):
        nums = [0, 1, 0, 1, 0]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testConsecutiveZerosAtStart(self):
        nums = [0, 0, 0, 1, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testConsecutiveZerosAtEnd(self):
        nums = [1, 1, 1, 0, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testConsecutiveZerosInMiddle(self):
        nums = [1, 1, 0, 0, 0, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 4)

    def testScatteredZeros(self):
        nums = [1, 0, 1, 0, 1, 0, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testAlternatingBits(self):
        nums = [0, 1, 0, 1, 0, 1, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testKLargerThanZeros(self):
        nums = [0, 1, 0, 1, 0]
        k = 10
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testThreeElements(self):
        nums = [1, 0, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testFourElements(self):
        nums = [1, 1, 0, 0]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testFiveElements(self):
        nums = [1, 0, 0, 0, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testLongSequenceOnes(self):
        nums = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 10)

    def testLongSequenceZeros(self):
        nums = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
        k = 5
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testMultipleValidWindows(self):
        nums = [1, 1, 0, 1, 1, 0, 1, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testZeroAtStartAndEnd(self):
        nums = [0, 1, 1, 1, 0]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 4)

    def testOnlyTwoZeros(self):
        nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 9)

    def testSixElements(self):
        nums = [1, 0, 1, 1, 0, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 4)

    def testSevenElements(self):
        nums = [0, 1, 1, 0, 1, 1, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testEightElements(self):
        nums = [1, 1, 1, 0, 0, 1, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 8)

    def testRepeatingPattern(self):
        nums = [1, 0, 1, 0, 1, 0, 1, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testMostlyOnes(self):
        nums = [1, 1, 1, 1, 0, 1, 1, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 8)

    def testMostlyZeros(self):
        nums = [0, 0, 0, 1, 0, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 3)

    def testLargeK(self):
        nums = [0, 0, 0, 1, 1, 0, 0]
        k = 100
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testKEqualsArrayLength(self):
        nums = [0, 0, 0, 0, 0]
        k = 5
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testSingleZero(self):
        nums = [1, 1, 1, 0, 1, 1, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testDoubleZeros(self):
        nums = [1, 1, 0, 0, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testTripleZeros(self):
        nums = [1, 0, 0, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testLongArray(self):
        nums = [1] * 50 + [0] * 10 + [1] * 50
        k = 10
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 110)

    def testWindowAtStart(self):
        nums = [0, 0, 1, 1, 1, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testWindowAtEnd(self):
        nums = [1, 1, 1, 1, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testComplexPattern(self):
        nums = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testAllZerosSmallK(self):
        nums = [0, 0, 0, 0, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 2)

    def testMaxAtStart(self):
        nums = [0, 0, 0, 1, 1, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testMaxAtEnd(self):
        nums = [1, 0, 1, 1, 0, 0, 0]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testMaxInMiddle(self):
        nums = [1, 0, 1, 0, 0, 0, 1, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testNoFlipsNeeded(self):
        nums = [1, 1, 1, 1]
        k = 5
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 4)

    def testExactlyKZeros(self):
        nums = [1, 0, 1, 0, 1, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testMoreThanKZeros(self):
        nums = [0, 0, 0, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 2)

    def testOneFlipNeeded(self):
        nums = [1, 1, 0, 1, 1]
        k = 1
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testTwoFlipsNeeded(self):
        nums = [1, 0, 1, 0, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testThreeFlipsNeeded(self):
        nums = [1, 0, 0, 0, 1]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testAsymmetricArray(self):
        nums = [1, 1, 1, 1, 0, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 6)

    def testSymmetricArray(self):
        nums = [0, 0, 1, 1, 1, 0, 0]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 5)

    def testVeryLongSequence(self):
        nums = [0] * 100 + [1] * 100
        k = 50
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 150)

    def testAlternatingLongSequence(self):
        nums = [0, 1] * 50
        k = 25
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 51)

    def testNineElements(self):
        nums = [1, 0, 1, 1, 0, 1, 1, 0, 1]
        k = 2
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)

    def testTenElements(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
        k = 3
        result = self.solution.longestOnes(nums, k)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()