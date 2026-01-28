import unittest
from pacific_atlantic_water_flow import Solution

class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicExample(self):
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testSingleCell(self):
        heights = [[1]]
        expected = [[0,0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def testSingleRow(self):
        heights = [[1,2,3]]
        expected = [[0,0],[0,1],[0,2]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testSingleColumn(self):
        heights = [[1],[2],[3]]
        expected = [[0,0],[1,0],[2,0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testAllSameHeight(self):
        heights = [[5,5,5],[5,5,5],[5,5,5]]
        expected = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testIncreasingHeights(self):
        heights = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[0,2],[1,2],[2,0],[2,1],[2,2]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def testDecreasingHeights(self):
        heights = [[9,8,7],[6,5,4],[3,2,1]]
        expected = [[0,0],[0,1],[0,2],[1,0],[2,0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def testTwoByTwo(self):
        heights = [[1,1],[1,1]]
        expected = [[0,0],[0,1],[1,0],[1,1]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testNoCommonCells(self):
        heights = [[10,10,10],[10,1,10],[10,10,10]]
        expected = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testMountainInMiddle(self):
        heights = [[1,2,3,2,1],[2,3,4,3,2],[3,4,5,4,3],[2,3,4,3,2],[1,2,3,2,1]]
        expected = [[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[4,0],[4,1],[4,2]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, expected)

    def testValleyInMiddle(self):
        heights = [[5,5,5,5,5],[5,1,1,1,5],[5,1,1,1,5],[5,1,1,1,5],[5,5,5,5,5]]
        expected = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,4],[2,0],[2,4],[3,0],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testLongRectangle(self):
        heights = [[1,2,3,4,5]]
        expected = [[0,0],[0,1],[0,2],[0,3],[0,4]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testTallRectangle(self):
        heights = [[1],[2],[3],[4],[5]]
        expected = [[0,0],[1,0],[2,0],[3,0],[4,0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))

    def testAlternatingHeights(self):
        heights = [[1,3,1],[3,1,3],[1,3,1]]
        expected = [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()