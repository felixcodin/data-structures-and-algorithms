import unittest
from intersection_of_two_arrays_ii import Solution


class TestIntersectionOfTwoArraysII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicIntersection(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [2, 2])

    def testWithDuplicates(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [4, 9])

    def testNoIntersection(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [])

    def testOneEmptyArray(self):
        nums1 = [1, 2, 3]
        nums2 = []
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [])

    def testBothEmptyArrays(self):
        nums1 = []
        nums2 = []
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [])

    def testSingleElementMatch(self):
        nums1 = [1]
        nums2 = [1]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [1])

    def testSingleElementNoMatch(self):
        nums1 = [1]
        nums2 = [2]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [])

    def testSubsetArray(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [2, 4]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [2, 4])

    def testAllSameElements(self):
        nums1 = [1, 1, 1, 1]
        nums2 = [1, 1]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [1, 1])

    def testMultipleOccurrences(self):
        nums1 = [3, 1, 2, 2, 3, 3]
        nums2 = [3, 3, 3, 2]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [2, 3, 3, 3])

    def testDifferentSizedArrays(self):
        nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums2 = [1, 3, 5]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [1, 3, 5])

    def testMoreDuplicatesInFirst(self):
        nums1 = [1, 1, 1, 1, 1]
        nums2 = [1, 1]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [1, 1])

    def testMoreDuplicatesInSecond(self):
        nums1 = [1, 1]
        nums2 = [1, 1, 1, 1, 1]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(result, [1, 1])

    def testLargerArrays(self):
        nums1 = [21, 45, 67, 12, 34, 56, 78, 90, 23, 45]
        nums2 = [45, 67, 89, 12, 56, 78, 45, 23]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [12, 23, 45, 45, 56, 67, 78])

    def testNegativeNumbers(self):
        nums1 = [-1, -2, -3, -4]
        nums2 = [-3, -4, -5]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [-4, -3])

    def testMixedPositiveNegative(self):
        nums1 = [-1, 0, 1, 2]
        nums2 = [0, 1, 2, 3]
        result = self.solution.intersect(nums1, nums2)
        self.assertEqual(sorted(result), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()