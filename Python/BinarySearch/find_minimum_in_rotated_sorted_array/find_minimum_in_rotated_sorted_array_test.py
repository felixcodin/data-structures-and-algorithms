import unittest
from find_minimum_in_rotated_sorted_array import Solution

class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        nums = [3,4,5,1,2]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testExampleCase2(self):
        nums = [4,5,6,7,0,1,2]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 0)

    def testExampleCase3(self):
        nums = [11,13,15,17]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 11)

    def testSingleElement(self):
        nums = [1]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testTwoElementsRotated(self):
        nums = [2,1]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testTwoElementsNotRotated(self):
        nums = [1,2]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testNotRotated(self):
        nums = [1,2,3,4,5]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testRotatedOnce(self):
        nums = [2,3,4,5,1]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testRotatedToEnd(self):
        nums = [5,1,2,3,4]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testLargerArray(self):
        nums = [7,8,9,10,11,12,1,2,3,4,5,6]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testMinAtBeginning(self):
        nums = [1,2,3,4,5,6,7]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

    def testMinAtEnd(self):
        nums = [2,1]
        res = self.solution.findMin(nums)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()