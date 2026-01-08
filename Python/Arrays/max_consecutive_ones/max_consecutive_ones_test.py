import unittest
from max_consecutive_ones import Solution

class TestMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testAllOnes(self):
        nums = [1, 1, 1, 1]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 4)

    def testAllZeros(self):
        nums = [0, 0, 0, 0]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 0)

    def testMixedWithMaxAtEnd(self):
        nums = [1, 0, 1, 1, 1]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 3)

    def testMixedWithMaxInMiddle(self):
        nums = [1, 1, 0, 1, 1, 1, 0, 1]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 3)

    def testSingleOne(self):
        nums = [1]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 1)

    def testSingleZero(self):
        nums = [0]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 0)

    def testEmptyArray(self):
        nums = []
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 0)

    def testAlternating(self):
        nums = [1, 0, 1, 0, 1, 0]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 1)

    def testMaxAtBeginning(self):
        nums = [1, 1, 1, 0, 1, 1]
        res = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()