import unittest
from top_K_frequent_element import Solution

class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2])

    def testSingleElement(self):
        nums = [1]
        k = 1
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, None)

    def testAllUniqueElements(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2, 3])

    def testAllElementsWithSameFrequency(self):
        nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        k = 1
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, None)   

    def testElementsWithIncreasingFrequency(self):
        nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        k = 2
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [4, 3])

    def testLargeKValue(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        k = 10
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def testElementsWithEqualFrequency(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 5
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2, 3, 4, 5])

    def testLargerArrayWithRepeatedElements(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2, 3])
    
    def testWorstCase(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
        k = 10
        res = self.solution.topKFrequent(nums, k)
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()