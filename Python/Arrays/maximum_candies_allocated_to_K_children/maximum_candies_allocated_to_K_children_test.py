import unittest
from maximum_candies_allocated_to_K_children import Solution

class TestMaximumCandies(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        candies = [5,8,6]
        k = 3
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 5)
    
    def testEdgeCase(self):
        candies = [10,5,8]
        k = 1
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 10)

    def testNoChildrenReceiveCandies(self):
        candies = [2,5]
        k = 11
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 0)
    
    def testNoPossibleDistribution(self):
        candies = [2,3]
        k = 5
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 1)

    def testLargeInputAndLargeK(self):
        candies = [100, 200, 300]
        k = 10
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 50)

    def testMinimumInput(self):
        candies = [1]
        k = 1
        res = self.solution.maximumCandies(candies, k)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()