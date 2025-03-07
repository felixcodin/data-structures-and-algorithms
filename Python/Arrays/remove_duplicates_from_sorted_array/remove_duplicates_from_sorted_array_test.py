import unittest
from remove_duplicates_from_sorted_array import Solution

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testExampleCase(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [0, 1, 2, 3, 4])

    def testNoDuplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, nums)
    
    def testAllElementAreTheSame(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [1])

    def testSingleElementArray(self):
        nums = [1]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, nums)

    def testTwoElementsNoDuplicates(self):
        nums = [1, 2]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, nums)

    def testTwoElementsWithDuplicates(self):
        nums = [5, 5]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [5])

    def testLargeArray(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def testArrayWithNegativeNumbers(self):
        nums = [-3, -3, -2, -2, -1, -1, 0, 0, 1, 1]
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [-3, -2, -1, 0, 1])

    def testEmptyArray(self):
        nums = []
        k = self.solution.removeDuplicates(nums)
        res = nums[:k]
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()