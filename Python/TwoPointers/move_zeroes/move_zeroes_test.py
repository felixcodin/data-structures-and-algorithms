import unittest
from move_zeroes import Solution


class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def testLeetCodeExample1(self):
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def testLeetCodeExample2(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def testNoZeros(self):
        nums = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def testAllZeros(self):
        nums = [0, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0])

    def testSingleNonZero(self):
        nums = [1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1])

    def testSingleZero(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def testTwoElements(self):
        nums = [0, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 0])

    def testTwoElementsNoZero(self):
        nums = [1, 2]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2])

    def testTwoElementsBothZeros(self):
        nums = [0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0])

    def testZeroAtBeginning(self):
        nums = [0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0])

    def testZeroAtEnd(self):
        nums = [1, 2, 3, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0])

    def testZeroInMiddle(self):
        nums = [1, 0, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0])

    def testMultipleZerosAtBeginning(self):
        nums = [0, 0, 0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testMultipleZerosAtEnd(self):
        nums = [1, 2, 3, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testMultipleZerosInMiddle(self):
        nums = [1, 0, 0, 0, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testAlternatingZeros(self):
        nums = [0, 1, 0, 2, 0, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testAlternatingZerosStartingWithNonZero(self):
        nums = [1, 0, 2, 0, 3, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testNegativeNumbers(self):
        nums = [0, -1, 0, -3, -12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, -3, -12, 0, 0])

    def testMixedPositiveNegative(self):
        nums = [0, 1, 0, -3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, -3, 12, 0, 0])

    def testAllNegatives(self):
        nums = [-1, -2, -3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, -2, -3])

    def testMixedWithZeroInMiddle(self):
        nums = [-1, 0, 2, -3, 0, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, 2, -3, 4, 0, 0])

    def testLargeNumbers(self):
        nums = [0, 100, 0, 200, 300]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [100, 200, 300, 0, 0])

    def testThreeElements(self):
        nums = [0, 0, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0])

    def testThreeElementsAllNonZero(self):
        nums = [1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3])

    def testThreeElementsAllZero(self):
        nums = [0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def testAlreadySorted(self):
        nums = [1, 2, 3, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testReverseSorted(self):
        nums = [0, 0, 0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def testSingleZeroMultipleNonZeros(self):
        nums = [1, 2, 0, 3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0])

    def testMultipleZerosSingleNonZero(self):
        nums = [0, 0, 1, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0, 0, 0])

    def testLongArray(self):
        nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 0, 0, 0, 0, 0])

    def testLongArrayNoZeros(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def testDuplicateNonZeros(self):
        nums = [0, 1, 1, 0, 2, 2]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 1, 2, 2, 0, 0])

    def testConsecutiveZeros(self):
        nums = [1, 0, 0, 0, 2]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 0, 0, 0])

    def testConsecutiveNonZeros(self):
        nums = [0, 1, 2, 3, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def testOnlyOneNonZero(self):
        nums = [0, 0, 0, 5, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [5, 0, 0, 0, 0, 0])

    def testOrderPreserved(self):
        nums = [4, 2, 0, 1, 0, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [4, 2, 1, 3, 0, 0])

    def testZerosScattered(self):
        nums = [0, 1, 0, 0, 2, 0, 3, 0, 0, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0, 0, 0, 0, 0, 0])

    def testHalfZeros(self):
        nums = [1, 0, 2, 0, 3, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()