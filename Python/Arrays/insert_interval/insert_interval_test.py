import unittest
from insert_interval import Solution

class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1,2],[3,10],[12,16]])
    
    def testInsertWithNoOverlap(self):
        intervals = [[1, 2], [5, 9], [10, 15]]
        newInterval = [3, 4]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1, 2], [3, 4], [5, 9], [10, 15]])
    
    def testInsertWithOverlap(self):
        intervals = [[1, 4], [6, 9], [10, 15]]
        newInterval = [2, 5]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1, 5], [6, 9], [10, 15]])
    
    def testInsertWithBeginning(self):
        intervals = [[2, 3], [5, 6], [8, 10], [12, 16]]
        newInterval = [0, 1]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[0, 1], [2, 3], [5, 6], [8, 10], [12, 16]])
    
    def testInsertWithTheEnd(self):
        intervals = [[1, 2], [4, 6]]
        newInterval = [8, 9]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1, 2], [4, 6], [8, 9]])

    def testinsertWithMultipleOverlap(self):
        intervals = [[1, 2], [4, 6], [7, 9], [10, 19]]
        newInterval = [3, 8]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1, 2], [3, 9], [10, 19]])

    def testInsertToAnEmptyList(self):
        intervals = []
        newInterval = [0, 10]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[0, 10]])

    def testInsertIntervalThatCoversAllExistingInterval(self):
        intervals = [[1, 2], [3, 4], [6, 9]]
        newInterval = [0, 10]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[0, 10]])

    def testInsertInside(self):
        intervals = [[1, 10]]
        newInterval = [2, 6]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[1, 10]])

    def testInsertIntervalOverlapsWithOneIntervalAndExtendsBeyond(self):
        intervals = [[2, 6], [8, 10]]
        newInterval = [5, 9]
        res = self.solution.insert(intervals, newInterval)
        self.assertEqual(res, [[2, 10]])

if __name__ == '__main__':
    unittest.main()