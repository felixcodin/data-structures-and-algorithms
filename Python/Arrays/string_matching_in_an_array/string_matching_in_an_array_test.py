import unittest
from string_matching_in_an_array import Solution

class TestStringMatchingInAnArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        words = ["mass", "as", "hero", "superhero"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["as", "hero"]))

    def testNoSubstrings(self):
        words = ["blue", "green", "bu"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, [])

    def testAllSubstrings(self):
        words = ["a", "aa", "aaa", "aaaa"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["a", "aa", "aaa"]))

    def testSingleWord(self):
        words = ["hello"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, [])

    def testIdenticalWords(self):
        words = ["abc", "abc"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, ["abc"])

    def testMultipleMatches(self):
        words = ["abc", "abcd", "abcde", "xyz"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["abc", "abcd"]))

    def testPartialOverlap(self):
        words = ["leetcode", "et", "code"]
        result = self.solution.stringMatching(words)
        self.assertEqual(sorted(result), sorted(["et", "code"]))

    def testEmptyArray(self):
        words = []
        result = self.solution.stringMatching(words)
        self.assertEqual(result, [])

    def testSubstringInMiddle(self):
        words = ["hello", "ell", "world"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, ["ell"])

    def testCaseSensitive(self):
        words = ["Abc", "abc", "bc"]
        result = self.solution.stringMatching(words)
        self.assertEqual(result, ["bc"])


if __name__ == '__main__':
    unittest.main()