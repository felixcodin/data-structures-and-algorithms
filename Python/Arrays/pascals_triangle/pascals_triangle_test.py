import unittest
from pascals_triangle import Solution

class TestPascalsTriangle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleRow(self):
        result = self.solution.generate(1)
        expected = [[1]]
        self.assertEqual(result, expected)

    def testTwoRows(self):
        result = self.solution.generate(2)
        expected = [[1], [1, 1]]
        self.assertEqual(result, expected)

    def testThreeRows(self):
        result = self.solution.generate(3)
        expected = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(result, expected)

    def testFiveRows(self):
        result = self.solution.generate(5)
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(result, expected)

    def testZeroRows(self):
        result = self.solution.generate(0)
        expected = []
        self.assertEqual(result, expected)

    def testSixRows(self):
        result = self.solution.generate(6)
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
        self.assertEqual(result, expected)

    def testRowLengths(self):
        result = self.solution.generate(5)
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1)

    def testEdgeValues(self):
        result = self.solution.generate(5)
        for row in result:
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def testSymmetry(self):
        result = self.solution.generate(7)
        for row in result:
            self.assertEqual(row, row[::-1])


if __name__ == '__main__':
    unittest.main()