import unittest
from number_of_islands import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleIsland(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testThreeIslands(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

    def testNoIslands(self):
        grid = [
            ["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def testAllIslands(self):
        grid = [
            ["1","1","1"],
            ["1","1","1"],
            ["1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testSingleCell(self):
        grid = [["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testSingleCellWater(self):
        grid = [["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def testVerticalIsland(self):
        grid = [
            ["1"],
            ["1"],
            ["1"],
            ["0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testHorizontalIsland(self):
        grid = [["1","1","1","0"]]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testMultipleDisconnectedIslands(self):
        grid = [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 8)

    def testDiagonalNotConnected(self):
        grid = [
            ["1","0","0"],
            ["0","1","0"],
            ["0","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

    def testLShapedIsland(self):
        grid = [
            ["1","1","0"],
            ["1","0","0"],
            ["1","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testComplexPattern(self):
        grid = [
            ["1","1","0","0","1"],
            ["1","0","0","1","1"],
            ["0","0","1","1","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 2)

    def testLargeGrid(self):
        grid = [
            ["1","0","1","0","1","0"],
            ["0","1","0","1","0","1"],
            ["1","0","1","0","1","0"],
            ["0","1","0","1","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 12)

    def testSurroundedIsland(self):
        grid = [
            ["0","0","0","0"],
            ["0","1","1","0"],
            ["0","1","1","0"],
            ["0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def testSnakeIsland(self):
        grid = [
            ["1","1","1","1","1"],
            ["0","0","0","0","1"],
            ["1","1","1","1","1"],
            ["1","0","0","0","0"],
            ["1","1","1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)


if __name__ == '__main__':
    unittest.main()