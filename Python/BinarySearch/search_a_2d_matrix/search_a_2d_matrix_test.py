import unittest
from search_a_2d_matrix import Solution

class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTargetExists(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 3))

    def testTargetDoesNotExist(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 13))

    def testTargetAtBeginning(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 1))

    def testTargetAtEnd(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 60))

    def testTargetInMiddleRow(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertTrue(self.solution.searchMatrix(matrix, 16))

    def testSingleElementMatrixTargetExists(self):
        matrix = [[5]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))

    def testSingleElementMatrixTargetDoesNotExist(self):
        matrix = [[5]]
        self.assertFalse(self.solution.searchMatrix(matrix, 1))

    def testSingleRowMatrixTargetExists(self):
        matrix = [[1,3,5,7,9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 7))

    def testSingleRowMatrixTargetDoesNotExist(self):
        matrix = [[1,3,5,7,9]]
        self.assertFalse(self.solution.searchMatrix(matrix, 4))

    def testSingleColumnMatrixTargetExists(self):
        matrix = [[1],[3],[5],[7],[9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))

    def testSingleColumnMatrixTargetDoesNotExist(self):
        matrix = [[1],[3],[5],[7],[9]]
        self.assertFalse(self.solution.searchMatrix(matrix, 6))

    def testTargetSmallerThanAllElements(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 0))

    def testTargetLargerThanAllElements(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 100))

    def testTargetBetweenRows(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        self.assertFalse(self.solution.searchMatrix(matrix, 8))

    def testLargerMatrix(self):
        matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
        self.assertTrue(self.solution.searchMatrix(matrix, 13))
        self.assertFalse(self.solution.searchMatrix(matrix, 21))

    def testConsecutiveNumbers(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertTrue(self.solution.searchMatrix(matrix, 5))
        self.assertTrue(self.solution.searchMatrix(matrix, 9))
        self.assertFalse(self.solution.searchMatrix(matrix, 10))

    def testTwoRowsMatrix(self):
        matrix = [[1,2],[3,6]]
        self.assertFalse(self.solution.searchMatrix(matrix, 4))
        self.assertTrue(self.solution.searchMatrix(matrix, 2))


if __name__ == '__main__':
    unittest.main()