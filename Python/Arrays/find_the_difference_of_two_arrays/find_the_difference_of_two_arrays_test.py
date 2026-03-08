import unittest
from find_the_difference_of_two_arrays import Solution


class TestFindDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3])
        self.assertEqual(sorted(result[1]), [4, 6])

    def testLeetCodeExample1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3])
        self.assertEqual(sorted(result[1]), [4, 6])

    def testLeetCodeExample2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [3])
        self.assertEqual(sorted(result[1]), [])

    def testBothEmpty(self):
        nums1 = []
        nums2 = []
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [])

    def testFirstEmpty(self):
        nums1 = []
        nums2 = [1, 2, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(sorted(result[1]), [1, 2, 3])

    def testSecondEmpty(self):
        nums1 = [1, 2, 3]
        nums2 = []
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(result[1], [])

    def testSingleElementBoth(self):
        nums1 = [1]
        nums2 = [2]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [2])

    def testSingleElementSame(self):
        nums1 = [1]
        nums2 = [1]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [])

    def testNoCommonElements(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [4, 5, 6])

    def testAllCommonElements(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [])

    def testWithDuplicatesInFirst(self):
        nums1 = [1, 1, 2, 2, 3, 3]
        nums2 = [2, 4, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3])
        self.assertEqual(sorted(result[1]), [4, 6])

    def testWithDuplicatesInSecond(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 2, 4, 4, 6, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3, 5])
        self.assertEqual(sorted(result[1]), [2, 4, 6])

    def testWithDuplicatesInBoth(self):
        nums1 = [1, 1, 2, 2, 3, 3]
        nums2 = [2, 2, 4, 4, 5, 5]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3])
        self.assertEqual(sorted(result[1]), [4, 5])

    def testNegativeNumbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-2, -4, -6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [-3, -1])
        self.assertEqual(sorted(result[1]), [-6, -4])

    def testMixedPositiveNegative(self):
        nums1 = [-1, 0, 1]
        nums2 = [0, 2, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [-1, 1])
        self.assertEqual(sorted(result[1]), [2, 3])

    def testWithZeros(self):
        nums1 = [0, 1, 2]
        nums2 = [0, 3, 4]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [3, 4])

    def testAllZeros(self):
        nums1 = [0, 0, 0]
        nums2 = [0, 0, 0]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [])

    def testFirstLonger(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7]
        nums2 = [2, 4]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3, 5, 6, 7])
        self.assertEqual(result[1], [])

    def testSecondLonger(self):
        nums1 = [1, 3]
        nums2 = [1, 2, 3, 4, 5, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(sorted(result[1]), [2, 4, 5, 6, 7])

    def testSubsetRelation(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4, 5]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(sorted(result[1]), [4, 5])

    def testSupersetRelation(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [4, 5])
        self.assertEqual(result[1], [])

    def testOverlappingRanges(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [3, 4, 5, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [5, 6])

    def testDisjointRanges(self):
        nums1 = [1, 2, 3]
        nums2 = [7, 8, 9]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [7, 8, 9])

    def testSingleCommonElement(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 5]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3])
        self.assertEqual(sorted(result[1]), [4, 5])

    def testMultipleCommonElements(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [2, 3, 4, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 5])
        self.assertEqual(sorted(result[1]), [6, 7])

    def testLargeNumbers(self):
        nums1 = [1000, 2000, 3000]
        nums2 = [2000, 4000, 5000]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1000, 3000])
        self.assertEqual(sorted(result[1]), [4000, 5000])

    def testConsecutiveNumbers(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [4, 5, 6, 7, 8]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [6, 7, 8])

    def testRepeatedSingleValue(self):
        nums1 = [5, 5, 5, 5]
        nums2 = [7, 7, 7, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [5])
        self.assertEqual(result[1], [7])

    def testManyDuplicates(self):
        nums1 = [1, 1, 1, 2, 2, 2]
        nums2 = [2, 2, 2, 3, 3, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [3])

    def testAlternatingPattern(self):
        nums1 = [1, 3, 5, 7, 9]
        nums2 = [2, 4, 6, 8, 10]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 3, 5, 7, 9])
        self.assertEqual(sorted(result[1]), [2, 4, 6, 8, 10])

    def testSymmetricDifference(self):
        nums1 = [1, 2, 5, 6]
        nums2 = [3, 4, 5, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [3, 4])

    def testOneElementEach(self):
        nums1 = [10]
        nums2 = [20]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [10])
        self.assertEqual(result[1], [20])

    def testTwoElementsEach(self):
        nums1 = [1, 2]
        nums2 = [2, 3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [3])

    def testThreeElementsEach(self):
        nums1 = [1, 2, 3]
        nums2 = [3, 4, 5]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [4, 5])

    def testNegativeZeroPositive(self):
        nums1 = [-1, 0, 1]
        nums2 = [-2, 0, 2]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [-1, 1])
        self.assertEqual(sorted(result[1]), [-2, 2])

    def testAllNegative(self):
        nums1 = [-5, -4, -3]
        nums2 = [-3, -2, -1]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [-5, -4])
        self.assertEqual(sorted(result[1]), [-2, -1])

    def testMirroredValues(self):
        nums1 = [1, 2, 3]
        nums2 = [-1, -2, -3]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [-3, -2, -1])

    def testLargeArray(self):
        nums1 = list(range(0, 100, 2))
        nums2 = list(range(1, 100, 2))
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), list(range(0, 100, 2)))
        self.assertEqual(sorted(result[1]), list(range(1, 100, 2)))

    def testMostlyCommon(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [11])

    def testFewCommon(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [5, 6, 7, 8, 9]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3, 4])
        self.assertEqual(sorted(result[1]), [6, 7, 8, 9])

    def testDuplicatesRemoved(self):
        nums1 = [1, 1, 1, 2, 3]
        nums2 = [3, 3, 3, 4, 5]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [4, 5])

    def testInterleavedValues(self):
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 3, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 5])
        self.assertEqual(sorted(result[1]), [2, 6])

    def testComplexPattern(self):
        nums1 = [10, 20, 30, 40, 50]
        nums2 = [15, 25, 30, 35, 45]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [10, 20, 40, 50])
        self.assertEqual(sorted(result[1]), [15, 25, 35, 45])

    def testSparseArrays(self):
        nums1 = [1, 100, 1000]
        nums2 = [10, 100, 10000]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 1000])
        self.assertEqual(sorted(result[1]), [10, 10000])

    def testDenseArrays(self):
        nums1 = [1, 2, 3, 4, 5, 6]
        nums2 = [4, 5, 6, 7, 8, 9]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [7, 8, 9])

    def testSingleOverlap(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [4, 5, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [5, 6, 7])

    def testNoOverlap(self):
        nums1 = [1, 2, 3]
        nums2 = [10, 20, 30]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2, 3])
        self.assertEqual(sorted(result[1]), [10, 20, 30])

    def testCompleteOverlap(self):
        nums1 = [5, 6, 7]
        nums2 = [5, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [])

    def testPartialOverlapWithDupes(self):
        nums1 = [1, 1, 2, 2, 3, 3]
        nums2 = [2, 2, 3, 3, 4, 4]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [4])

    def testMixedSizes(self):
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(result[0], [1])
        self.assertEqual(sorted(result[1]), [2, 3, 4, 5, 6])

    def testReversedRanges(self):
        nums1 = [5, 4, 3, 2, 1]
        nums2 = [3, 4, 5, 6, 7]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [1, 2])
        self.assertEqual(sorted(result[1]), [6, 7])

    def testBoundaryValues(self):
        nums1 = [-1000, 0, 1000]
        nums2 = [0, 500, 1500]
        result = self.solution.findDifference(nums1, nums2)
        self.assertEqual(sorted(result[0]), [-1000, 1000])
        self.assertEqual(sorted(result[1]), [500, 1500])


if __name__ == '__main__':
    unittest.main()