import unittest
from find_the_highest_altitude import Solution


class TestLargestAltitude(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        gain = [-5, 1, 5, 0, -7]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 1)

    def testLeetCodeExample1(self):
        gain = [-5, 1, 5, 0, -7]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 1)

    def testLeetCodeExample2(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testSinglePositive(self):
        gain = [5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testSingleNegative(self):
        gain = [-5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testSingleZero(self):
        gain = [0]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testAllPositive(self):
        gain = [1, 2, 3, 4, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 15)

    def testAllNegative(self):
        gain = [-1, -2, -3, -4, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testAllZeros(self):
        gain = [0, 0, 0, 0]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testMaxAtStart(self):
        gain = [10, -5, -3, -2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testMaxAtEnd(self):
        gain = [1, 2, 3, 4, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 15)

    def testMaxInMiddle(self):
        gain = [5, 5, -8, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testMaxAtInitialAltitude(self):
        gain = [-1, -2, -3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testTwoElements(self):
        gain = [5, -3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testTwoElementsNegative(self):
        gain = [-5, -3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testTwoElementsPositive(self):
        gain = [3, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testAlternatingPositiveNegative(self):
        gain = [5, -3, 4, -2, 1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 6)

    def testAlternatingNegativePositive(self):
        gain = [-5, 10, -3, 8]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testLargePositiveGain(self):
        gain = [100, -50, 25]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 100)

    def testLargeNegativeGain(self):
        gain = [-100, 50, -25]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testGoDownThenUp(self):
        gain = [-10, 5, 5, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testGoUpThenDown(self):
        gain = [10, -5, -5, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testMixedValues(self):
        gain = [1, -1, 2, -2, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 3)

    def testZerosAtStart(self):
        gain = [0, 0, 5, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testZerosAtEnd(self):
        gain = [5, 3, 0, 0]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testZerosInMiddle(self):
        gain = [5, 0, 0, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testThreeElements(self):
        gain = [3, 4, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 12)

    def testFourElements(self):
        gain = [1, 2, 3, 4]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testFiveElements(self):
        gain = [2, 2, 2, 2, 2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testNegativeToPositive(self):
        gain = [-5, -3, 10, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 7)

    def testPositiveToNegative(self):
        gain = [5, 3, -10, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testSumToZero(self):
        gain = [5, -5, 3, -3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testSumToPositive(self):
        gain = [5, -2, 3, -1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 6)

    def testSumToNegative(self):
        gain = [5, -10, 2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testLongIncreasing(self):
        gain = [1, 1, 1, 1, 1, 1, 1, 1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testLongDecreasing(self):
        gain = [-1, -1, -1, -1, -1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)

    def testMountainPattern(self):
        gain = [3, 3, 3, -2, -2, -2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 9)

    def testValleyPattern(self):
        gain = [-3, -3, 5, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 4)

    def testPeakInMiddle(self):
        gain = [5, 10, -8, -7]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 15)

    def testMultiplePeaks(self):
        gain = [5, -3, 4, -2, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 7)

    def testStepUp(self):
        gain = [1, 2, 3, 4, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 15)

    def testStepDown(self):
        gain = [5, -1, -1, -1, -1, -1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testSmallGains(self):
        gain = [1, 1, 1, 1]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 4)

    def testLargeGains(self):
        gain = [100, 100, 100]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 300)

    def testMixedSmallLarge(self):
        gain = [1, 100, -50, 10]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 101)

    def testRepeatedValues(self):
        gain = [5, 5, 5, -15]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 15)

    def testSymmetricGain(self):
        gain = [5, 3, -3, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 8)

    def testAsymmetricGain(self):
        gain = [10, -5, 3, -8]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testEqualPositiveNegative(self):
        gain = [5, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 5)

    def testGradualIncrease(self):
        gain = [1, 2, 3, 4]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testGradualDecrease(self):
        gain = [4, -1, -2, -3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 4)

    def testZigZag(self):
        gain = [2, -1, 3, -2, 4]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 6)

    def testLargeArray(self):
        gain = [1] * 50 + [-1] * 25
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 50)

    def testStartHigh(self):
        gain = [100, -10, -20, -30]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 100)

    def testStartLow(self):
        gain = [-50, 60, 10, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 25)

    def testNetZeroGain(self):
        gain = [10, -5, -5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testNetPositiveGain(self):
        gain = [10, -3, 5]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 12)

    def testNetNegativeGain(self):
        gain = [10, -15, 3]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testSixElements(self):
        gain = [1, 2, -1, 3, -2, 4]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 7)

    def testSevenElements(self):
        gain = [5, -2, 3, -1, 4, -3, 2]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 9)

    def testEightElements(self):
        gain = [2, 3, -4, 5, -2, 3, -1, 4]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 10)

    def testMinimalPositive(self):
        gain = [1, 0, 0, 0]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 1)

    def testMinimalNegative(self):
        gain = [-1, 0, 0, 0]
        result = self.solution.largestAltitude(gain)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()