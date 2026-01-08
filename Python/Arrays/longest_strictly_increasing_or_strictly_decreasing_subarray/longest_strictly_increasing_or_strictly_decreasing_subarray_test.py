import unittest
from longest_strictly_increasing_or_strictly_decreasing_subarray import Solution

class TestLongestMonotonicSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleElement(self):
        nums = [1]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 1)

    def testStrictlyIncreasing(self):
        nums = [1, 2, 3, 4, 5]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 5)

    def testStrictlyDecreasing(self):
        nums = [5, 4, 3, 2, 1]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 5)

    def testMixedIncreasingAndDecreasing(self):
        nums = [1, 4, 3, 3, 2]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 2)

    def testAllEqualElements(self):
        nums = [3, 3, 3, 3]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 1)

    def testTwoElements(self):
        nums = [1, 2]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 2)

    def testAlternatingPattern(self):
        nums = [1, 3, 2, 4, 3]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 2)

    def testLongIncreasingThenDecreasing(self):
        nums = [1, 2, 3, 4, 3, 2, 1]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 4)

    def testLongDecreasingThenIncreasing(self):
        nums = [5, 4, 3, 2, 3, 4, 5]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 4)

    def testEqualElementsInMiddle(self):
        nums = [1, 2, 3, 3, 4, 5]
        res = self.solution.longestMonotonicSubarray(nums)
        self.assertEqual(res, 3)

if __name__ == '__main__':
    unittest.main()