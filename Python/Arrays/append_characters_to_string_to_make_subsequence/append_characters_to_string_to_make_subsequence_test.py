import unittest
from append_characters_to_string_to_make_subsequence import Solution

class TestAppendCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        s = "coaching"
        t = "coding"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 4)

    def testExampleCase2(self):
        s = "abcde"
        t = "a"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testExampleCase3(self):
        s = "z"
        t = "abcde"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 5)

    def testEmptyS(self):
        s = ""
        t = "abc"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 3)

    def testEmptyT(self):
        s = "abc"
        t = ""
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testBothEmpty(self):
        s = ""
        t = ""
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testCompleteSubsequence(self):
        s = "abcdef"
        t = "ace"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testNoMatchingCharacters(self):
        s = "abc"
        t = "xyz"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 3)

    def testPartialMatch(self):
        s = "abcde"
        t = "acdeg"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 1)

    def testSameStrings(self):
        s = "hello"
        t = "hello"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testSingleCharacterMatch(self):
        s = "a"
        t = "a"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 0)

    def testSingleCharacterNoMatch(self):
        s = "a"
        t = "b"
        res = self.solution.appendCharacters(s, t)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()