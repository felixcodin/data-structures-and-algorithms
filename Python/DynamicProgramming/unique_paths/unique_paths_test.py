import unittest
from unique_paths import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testOneByOneGrid(self):
        # Only one path in a 1x1 grid
        result = self.solution.uniquePaths(1, 1)
        self.assertEqual(result, 1)

    def testOneRowGrid(self):
        # Only one path when there's only one row
        result = self.solution.uniquePaths(1, 5)
        self.assertEqual(result, 1)

    def testOneColumnGrid(self):
        # Only one path when there's only one column
        result = self.solution.uniquePaths(5, 1)
        self.assertEqual(result, 1)

    def testTwoByTwoGrid(self):
        # 2x2 grid has 2 unique paths
        result = self.solution.uniquePaths(2, 2)
        self.assertEqual(result, 2)

    def testTwoByThreeGrid(self):
        # 2x3 grid has 3 unique paths
        result = self.solution.uniquePaths(2, 3)
        self.assertEqual(result, 3)

    def testThreeByTwoGrid(self):
        # 3x2 grid has 3 unique paths (symmetric to 2x3)
        result = self.solution.uniquePaths(3, 2)
        self.assertEqual(result, 3)

    def testThreeByThreeGrid(self):
        # 3x3 grid has 6 unique paths
        result = self.solution.uniquePaths(3, 3)
        self.assertEqual(result, 6)

    def testLeetCodeExample1(self):
        # Example from LeetCode: m = 3, n = 7
        result = self.solution.uniquePaths(3, 7)
        self.assertEqual(result, 28)

    def testLeetCodeExample2(self):
        # Example from LeetCode: m = 3, n = 2
        result = self.solution.uniquePaths(3, 2)
        self.assertEqual(result, 3)

    def testFourByFourGrid(self):
        # 4x4 grid has 20 unique paths
        result = self.solution.uniquePaths(4, 4)
        self.assertEqual(result, 20)

    def testFiveByFiveGrid(self):
        # 5x5 grid has 70 unique paths
        result = self.solution.uniquePaths(5, 5)
        self.assertEqual(result, 70)

    def testTwoByFiveGrid(self):
        # 2x5 grid has 5 unique paths
        result = self.solution.uniquePaths(2, 5)
        self.assertEqual(result, 5)

    def testFiveByTwoGrid(self):
        # 5x2 grid has 5 unique paths (symmetric to 2x5)
        result = self.solution.uniquePaths(5, 2)
        self.assertEqual(result, 5)

    def testSevenByThreeGrid(self):
        # 7x3 grid should equal 3x7 grid (symmetry test)
        result = self.solution.uniquePaths(7, 3)
        self.assertEqual(result, 28)

    def testLargerGrid(self):
        # 10x10 grid has 48620 unique paths
        result = self.solution.uniquePaths(10, 10)
        self.assertEqual(result, 48620)

    def testRectangularGrid1(self):
        # 4x6 grid
        result = self.solution.uniquePaths(4, 6)
        self.assertEqual(result, 56)

    def testRectangularGrid2(self):
        # 6x4 grid (symmetric to 4x6)
        result = self.solution.uniquePaths(6, 4)
        self.assertEqual(result, 56)

    def testMinimumValidInput(self):
        # Test with minimum valid grid sizes
        result = self.solution.uniquePaths(1, 2)
        self.assertEqual(result, 1)

    def testAsymmetricGrid(self):
        # 2x10 grid
        result = self.solution.uniquePaths(2, 10)
        self.assertEqual(result, 10)

    def testMediumGrid(self):
        # 5x7 grid
        result = self.solution.uniquePaths(5, 7)
        self.assertEqual(result, 210)

    def testLargerAsymmetric(self):
        # 8x5 grid
        result = self.solution.uniquePaths(8, 5)
        self.assertEqual(result, 330)


if __name__ == '__main__':
    unittest.main()