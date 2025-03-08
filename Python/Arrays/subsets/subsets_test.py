import unittest
from subsets import Solution

class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testExampleCase(self):
        nums = [1, 2, 3]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def testSingleElementArray(self):
        nums = [1]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [1]])

    def testTwoElementsArray(self):
        nums = [1, 2]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [1], [2], [1, 2]])

    def testEmptyArray(self):
        nums = []
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[]])

    def testFourElementsArray(self):
        nums = [1, 2, 3, 4]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]])

    def testNegativeArray(self):
        nums = [-1, -2, -3]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [-1], [-2], [-1, -2], [-3], [-1, -3], [-2, -3], [-1, -2, -3]])

    def testArrayWithMixed(self):
        nums = [-1, 0, 1]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]])

    def testDuplicateElements(self):
        nums = [10, 10]
        res = self.solution.subsets(nums)
        self.assertEqual(res, [[], [10], [10], [10, 10]])

if __name__ == '__main__':
    unittest.main()