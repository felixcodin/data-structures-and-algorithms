import unittest
from longest_subarray_of_1s_after_deleting_one_element import Solution


class TestLongestSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testLeetCodeExample1(self):
        nums = [1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testLeetCodeExample2(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testLeetCodeExample3(self):
        nums = [1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testAllOnes(self):
        nums = [1, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testAllZeros(self):
        nums = [0, 0, 0, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 0)

    def testSingleOne(self):
        nums = [1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 0)

    def testSingleZero(self):
        nums = [0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 0)

    def testTwoOnes(self):
        nums = [1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 1)

    def testTwoZeros(self):
        nums = [0, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 0)

    def testOneZeroOneOne(self):
        nums = [0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 1)

    def testOneOneZero(self):
        nums = [1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 1)

    def testSingleZeroInMiddle(self):
        nums = [1, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 6)

    def testSingleZeroAtStart(self):
        nums = [0, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testSingleZeroAtEnd(self):
        nums = [1, 1, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testTwoZerosSeparated(self):
        nums = [1, 1, 0, 1, 1, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testTwoZerosConsecutive(self):
        nums = [1, 1, 0, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testThreeZeros(self):
        nums = [1, 0, 1, 0, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testAlternating(self):
        nums = [0, 1, 0, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testAlternatingStartWithOne(self):
        nums = [1, 0, 1, 0, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testThreeElements(self):
        nums = [1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testFourElements(self):
        nums = [1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testFiveElements(self):
        nums = [1, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testMostlyOnes(self):
        nums = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 9)

    def testMostlyZeros(self):
        nums = [0, 0, 0, 1, 0, 0, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 1)

    def testLongSequenceOfOnes(self):
        nums = [1] * 10 + [0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 12)

    def testLongSequenceOfZeros(self):
        nums = [1, 1] + [0] * 10
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testZeroAtBothEnds(self):
        nums = [0, 1, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testMultipleZerosAtStart(self):
        nums = [0, 0, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testMultipleZerosAtEnd(self):
        nums = [1, 1, 1, 0, 0, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testMultipleZerosInMiddle(self):
        nums = [1, 1, 0, 0, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testSixElements(self):
        nums = [1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testSevenElements(self):
        nums = [1, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 6)

    def testEightElements(self):
        nums = [1, 0, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testComplexPattern1(self):
        nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testComplexPattern2(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testMaxAtStart(self):
        nums = [1, 1, 1, 1, 0, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testMaxAtEnd(self):
        nums = [1, 0, 0, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testMaxInMiddle(self):
        nums = [1, 0, 1, 1, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testTwoOnesOneZero(self):
        nums = [1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testOneZeroTwoOnes(self):
        nums = [0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testSymmetricArray(self):
        nums = [1, 1, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testAsymmetricArray(self):
        nums = [1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testLargeArrayAllOnes(self):
        nums = [1] * 100
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 99)

    def testLargeArrayAllZeros(self):
        nums = [0] * 100
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 0)

    def testLargeArrayWithOneZero(self):
        nums = [1] * 50 + [0] + [1] * 50
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 100)

    def testLargeArrayWithTwoZeros(self):
        nums = [1] * 30 + [0] + [1] * 20 + [0] + [1] * 30
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 50)

    def testNineElements(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testTenElements(self):
        nums = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testConsecutiveOnesAfterZero(self):
        nums = [0, 1, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testConsecutiveOnesBeforeZero(self):
        nums = [1, 1, 1, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testRepeatingPattern(self):
        nums = [1, 0, 1, 0, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testLongOnesShortZeros(self):
        nums = [1, 1, 1, 1, 0, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 8)

    def testShortOnesLongZeros(self):
        nums = [1, 0, 0, 0, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 1)

    def testDeleteFirstElement(self):
        nums = [1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testDeleteLastElement(self):
        nums = [1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testTwoSeparateGroups(self):
        nums = [1, 1, 0, 0, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testThreeSeparateGroups(self):
        nums = [1, 0, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testFourSeparateGroups(self):
        nums = [1, 0, 1, 0, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 2)

    def testOnlyOnesBetweenZeros(self):
        nums = [0, 1, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testWindowSliding(self):
        nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 6)

    def testMultipleValidWindows(self):
        nums = [1, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 6)

    def testStartWithZero(self):
        nums = [0, 1, 1, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testEndWithZero(self):
        nums = [1, 1, 1, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testZeroEveryThirdPosition(self):
        nums = [1, 1, 0, 1, 1, 0, 1, 1, 0]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 4)

    def testIncreasingOnes(self):
        nums = [1, 0, 1, 1, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testDecreasingOnes(self):
        nums = [1, 1, 1, 0, 1, 1, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 5)

    def testEdgeCase1(self):
        nums = [1, 0, 0, 1, 1, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)

    def testEdgeCase2(self):
        nums = [1, 1, 1, 0, 0, 1]
        result = self.solution.longestSubarray(nums)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()