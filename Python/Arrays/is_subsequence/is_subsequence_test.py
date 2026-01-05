import unittest
from is_subsequence import Solution

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testEmptySubsequence(self):
        s = ""
        t = "abc"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testEmptyTarget(self):
        s = "abc"
        t = ""
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, False)

    def testBothEmpty(self):
        s = ""
        t = ""
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testExactMatch(self):
        s = "abc"
        t = "abc"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testValidSubsequence(self):
        s = "abc"
        t = "ahbgdc"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testInvalidSubsequence(self):
        s = "axc"
        t = "ahbgdc"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, False)

    def testSingleCharacterMatch(self):
        s = "a"
        t = "a"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testSingleCharacterNoMatch(self):
        s = "a"
        t = "b"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, False)

    def testLongerSubsequence(self):
        s = "abc"
        t = "ab"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, False)

    def testRepeatedCharacters(self):
        s = "aaa"
        t = "aaaa"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testSubsequenceAtEnd(self):
        s = "def"
        t = "abcdef"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

    def testSubsequenceAtStart(self):
        s = "abc"
        t = "abcdef"
        res = self.solution.isSubsequence(s, t)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()