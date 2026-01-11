import unittest
from container_with_most_water import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 49)

    def testTwoElements(self):
        heights = [1, 1]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 1)

    def testIncreasingHeights(self):
        heights = [1, 2, 3, 4, 5]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 6)

    def testDecreasingHeights(self):
        heights = [5, 4, 3, 2, 1]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 6)

    def testAllSameHeight(self):
        heights = [5, 5, 5, 5, 5]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 20)

    def testMaxAtEnds(self):
        heights = [8, 1, 1, 1, 8]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 32)

    def testMaxInMiddle(self):
        heights = [1, 3, 2, 5, 25, 24, 5]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 24)

    def testLargeGap(self):
        heights = [1, 2, 1]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 2)

    def testSingleTallBar(self):
        heights = [1, 100, 1]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()