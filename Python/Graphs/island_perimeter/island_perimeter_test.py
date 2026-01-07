import unittest
from island_perimeter import Solution

class TestIslandPerimeter(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        grid = [[0,1,0,0],
                [1,1,1,0],
                [0,1,0,0],
                [1,1,0,0]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 16)

    def testExampleCase2(self):
        grid = [[1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 4)

    def testExampleCase3(self):
        grid = [[1,0]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 4)

    def testSingleRow(self):
        grid = [[1,1,1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 8)

    def testSingleColumn(self):
        grid = [[1],
                [1],
                [1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 8)

    def testSquareIsland(self):
        grid = [[1,1],
                [1,1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 8)

    def testLShapedIsland(self):
        grid = [[1,1],
                [1,0]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 8)

    def testAllWater(self):
        grid = [[0,0],
                [0,0]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 0)

    def testIslandWithHole(self):
        grid = [[1,1,1],
                [1,0,1],
                [1,1,1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 16)

    def testDiagonalCells(self):
        grid = [[1,0,0],
                [0,1,0],
                [0,0,1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 12)

    def testLargeConnectedIsland(self):
        grid = [[1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]]
        res = self.solution.islandPerimeter(grid)
        self.assertEqual(res, 14)

if __name__ == '__main__':
    unittest.main()