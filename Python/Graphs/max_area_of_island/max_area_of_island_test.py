import unittest
from max_area_of_island import Solution

class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 6)

    def testAllZeros(self):
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 0)

    def testAllOnes(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 9)

    def testSingleCell(self):
        grid = [[1]]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 1)

    def testSingleCellZero(self):
        grid = [[0]]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 0)

    def testMultipleIslands(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 4)

    def testSingleRowIsland(self):
        grid = [[1, 1, 1, 1, 1]]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 5)

    def testSingleColumnIsland(self):
        grid = [[1], [1], [1], [1]]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 4)

    def testLShapedIsland(self):
        grid = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 5)

    def testDisconnectedCells(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()