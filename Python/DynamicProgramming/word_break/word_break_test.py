import unittest
from word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testCannotBreak(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertFalse(result)

    def testSingleWord(self):
        s = "apple"
        wordDict = ["apple"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testMultipleWaysToBreak(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testEmptyString(self):
        s = ""
        wordDict = ["apple", "pen"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testWordReuse(self):
        s = "aaaaaaa"
        wordDict = ["aaaa", "aaa"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testOverlappingWords(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testSingleCharacter(self):
        s = "a"
        wordDict = ["a"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testNoMatch(self):
        s = "cars"
        wordDict = ["car", "ca", "rs"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testLongerWords(self):
        s = "abcd"
        wordDict = ["a", "abc", "b", "cd"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testPartialMatchOnly(self):
        s = "goalspecial"
        wordDict = ["go", "goal", "goals", "special"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def testComplexFalseCase(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()