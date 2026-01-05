import unittest
from length_of_last_word import Solution

class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        s = "Hello World"
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 5)
    
    def testSingleWord(self):
        s = "Hello"
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 5)

    def testTrailingSpaces(self):
        s = "Hello World   "
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 5)

    def testMultipleSpacesBetweenWords(self):
        s = "Hello    World"
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 5)

    def testEmptyString(self):
        s = ""
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 0)

    def testOnlySpaces(self):
        s = "     "
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 0)

    def testSingleCharacter(self):
        s = "a"
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 1)

    def testLeadingAndTrailingSpaces(self):
        s = "   fly me   to   the moon  "
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 4)

    def testMultipleWords(self):
        s = "luffy is still joyboy"
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 6)

    def testSingleSpaceAtEnd(self):
        s = "test "
        res = self.solution.lengthOfLastWord(s)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()