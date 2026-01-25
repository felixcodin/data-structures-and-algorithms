import unittest
from word_search import Solution

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicWordFound(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertTrue(self.solution.exist(board, "ABCCED"))

    def testBasicWordNotFound(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertFalse(self.solution.exist(board, "ABCB"))

    def testSimpleWordFound(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        self.assertTrue(self.solution.exist(board, "SEE"))

    def testSingleCharacterBoard(self):
        board = [["A"]]
        self.assertTrue(self.solution.exist(board, "A"))
        self.assertFalse(self.solution.exist(board, "B"))

    def testSingleCharacterWord(self):
        board = [["A","B"],["C","D"]]
        self.assertTrue(self.solution.exist(board, "A"))
        self.assertTrue(self.solution.exist(board, "D"))

    def testWordLongerThanBoard(self):
        board = [["A","B"]]
        self.assertFalse(self.solution.exist(board, "ABCD"))

    def testHorizontalWord(self):
        board = [["A","B","C","D"]]
        self.assertTrue(self.solution.exist(board, "ABCD"))

    def testVerticalWord(self):
        board = [["A"],["B"],["C"],["D"]]
        self.assertTrue(self.solution.exist(board, "ABCD"))

    def testZigzagPath(self):
        board = [["A","B","C"],["D","E","F"],["G","H","I"]]
        self.assertTrue(self.solution.exist(board, "ABEF"))

    def testRepeatedCharacters(self):
        board = [["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]]
        self.assertTrue(self.solution.exist(board, "AAAAAAAAA"))

    def testCannotReuseSameCell(self):
        board = [["A","B"],["C","D"]]
        self.assertFalse(self.solution.exist(board, "ABCDA"))

    def testComplexPath(self):
        board = [["C","A","A"],["A","A","A"],["B","C","D"]]
        self.assertTrue(self.solution.exist(board, "AAB"))

    def testWordWithBacktracking(self):
        board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        self.assertTrue(self.solution.exist(board, "ABCESEEEFS"))

    def testEmptyWord(self):
        board = [["A","B"],["C","D"]]
        self.assertTrue(self.solution.exist(board, ""))

    def testStartFromDifferentPositions(self):
        board = [["A","B","C"],["D","E","F"],["G","H","I"]]
        self.assertTrue(self.solution.exist(board, "EFI"))

    def testNoValidPath(self):
        board = [["A","B"],["C","D"]]
        self.assertFalse(self.solution.exist(board, "AD"))

    def testWordRequiresFullBacktracking(self):
        board = [["A","A","A","A"],["A","B","B","A"],["A","B","B","A"],["A","A","A","A"]]
        self.assertTrue(self.solution.exist(board, "AAAAAAAA"))

    def testLargerBoard(self):
        board = [
            ["A","B","C","E","F"],
            ["S","F","C","S","G"],
            ["A","D","E","E","H"]
        ]
        self.assertTrue(self.solution.exist(board, "ABCCED"))

    def testSpiralPath(self):
        board = [["A","B","C"],["H","I","D"],["G","F","E"]]
        self.assertTrue(self.solution.exist(board, "ABCDEFGHI"))

    def testMultiplePathsOnlyOneValid(self):
        board = [["A","A"],["A","B"]]
        self.assertTrue(self.solution.exist(board, "AAB"))


if __name__ == '__main__':
    unittest.main()