import unittest
from search_in_rotated_sorted_array import Solution

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        res = self.solution.search(nums, target)
        self.assertEqual(res, 4)

    def testTargetInLeftPortion(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 5
        res = self.solution.search(nums, target)
        self.assertEqual(res, 1)

    def testTargetInRightPortion(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 1
        res = self.solution.search(nums, target)
        self.assertEqual(res, 5)

    def testTargetNotFound(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        res = self.solution.search(nums, target)
        self.assertEqual(res, -1)

    def testNoRotation(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        res = self.solution.search(nums, target)
        self.assertEqual(res, 2)

    def testSingleElement(self):
        nums = [1]
        target = 1
        res = self.solution.search(nums, target)
        self.assertEqual(res, 0)

    def testSingleElementNotFound(self):
        nums = [1]
        target = 0
        res = self.solution.search(nums, target)
        self.assertEqual(res, -1)

    def testTwoElements(self):
        nums = [3, 1]
        target = 1
        res = self.solution.search(nums, target)
        self.assertEqual(res, 1)

    def testTargetAtBeginning(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        res = self.solution.search(nums, target)
        self.assertEqual(res, 0)

    def testTargetAtEnd(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        res = self.solution.search(nums, target)
        self.assertEqual(res, 6)

    def testLargeRotation(self):
        nums = [5, 1, 2, 3, 4]
        target = 1
        res = self.solution.search(nums, target)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()