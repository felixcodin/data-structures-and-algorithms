import unittest
from valid_word_square import Solution

class TestValidWordSquare(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        words = ["abcd", "bnrt", "crmy", "dtye"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testExampleCase2(self):
        words = ["abcd", "bnrt", "crm", "dt"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testExampleCase3(self):
        words = ["ball", "area", "read", "lady"]
        res = self.solution.validWordSquare(words)
        self.assertFalse(res)

    def testEmptyList(self):
        words = []
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testSingleWord(self):
        words = ["a"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testUnequalRowsAndColumns(self):
        words = ["abc", "b"]
        res = self.solution.validWordSquare(words)
        self.assertFalse(res)

    def testDifferentLengthRows(self):
        words = ["abc", "de", "f"]
        res = self.solution.validWordSquare(words)
        self.assertFalse(res)

    def testValidSquare2x2(self):
        words = ["ab", "ba"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testInvalidSquare2x2(self):
        words = ["ab", "bc"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testValidSquare3x3(self):
        words = ["abc", "bde", "cef"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testMissingCharacters(self):
        words = ["abcd", "b", "c", "d"]
        res = self.solution.validWordSquare(words)
        self.assertTrue(res)

    def testRowLongerThanNumberOfRows(self):
        words = ["abcde", "b"]
        res = self.solution.validWordSquare(words)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()