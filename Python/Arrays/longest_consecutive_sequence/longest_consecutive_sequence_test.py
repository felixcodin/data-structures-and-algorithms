import unittest
from longest_consecutive_sequence import Solution

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [100, 4, 200, 1, 3, 2]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 4)

    def testArrayWithDuplicatedElements(self):
        nums = [0, 3, 2, 5, 4, 6, 1, 1]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 7)

    def testNegativeAndPositiveNumbers(self):
        nums = [-1, -2, -3, 0, 1, 2, 3]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 7)

    def testSameElements(self):
        nums = [1, 1, 1, 1]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 1)

    def testNoConsecutiveSequence(self):
        nums = [10, 20, 30, 40]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 1)

    def testEmptyArray(self):
        nums = []
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 0)

    def testArrayWithOneElement(self):
        nums = [5]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 1)

    def testArrayWithTwoElement(self):
        nums = [1, 2]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 2)

    def testLargeRangeOfNumber(self):
        nums = [10, 5, 12, 3, 55, 30, 4, 11, 6, 7, 8, 9]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 10)
        
    def testNegativeNumbersOnly(self):
        nums = [-5, -4, -3, -2, -1]
        res = self.solution.longestConsecutive(nums)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()