import unittest
from longest_common_subsequence import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLeetCodeExample1(self):
        # "ace" is the longest common subsequence
        result = self.solution.longestCommonSubsequence("abcde", "ace")
        self.assertEqual(result, 3)

    def testLeetCodeExample2(self):
        # "a" is the longest common subsequence
        result = self.solution.longestCommonSubsequence("abc", "abc")
        self.assertEqual(result, 3)

    def testLeetCodeExample3(self):
        # No common subsequence
        result = self.solution.longestCommonSubsequence("abc", "def")
        self.assertEqual(result, 0)

    def testBothEmptyStrings(self):
        result = self.solution.longestCommonSubsequence("", "")
        self.assertEqual(result, 0)

    def testFirstStringEmpty(self):
        result = self.solution.longestCommonSubsequence("", "abc")
        self.assertEqual(result, 0)

    def testSecondStringEmpty(self):
        result = self.solution.longestCommonSubsequence("abc", "")
        self.assertEqual(result, 0)

    def testSingleCharacterMatch(self):
        result = self.solution.longestCommonSubsequence("a", "a")
        self.assertEqual(result, 1)

    def testSingleCharacterNoMatch(self):
        result = self.solution.longestCommonSubsequence("a", "b")
        self.assertEqual(result, 0)

    def testIdenticalStrings(self):
        result = self.solution.longestCommonSubsequence("abcdef", "abcdef")
        self.assertEqual(result, 6)

    def testCompletelyDifferent(self):
        result = self.solution.longestCommonSubsequence("xyz", "abc")
        self.assertEqual(result, 0)

    def testOneCharacterCommon(self):
        result = self.solution.longestCommonSubsequence("abcd", "efga")
        self.assertEqual(result, 1)

    def testSubsequenceAtEnd(self):
        result = self.solution.longestCommonSubsequence("abcde", "xyz")
        self.assertEqual(result, 0)

    def testRepeatedCharacters(self):
        result = self.solution.longestCommonSubsequence("aaa", "aa")
        self.assertEqual(result, 2)

    def testAlternatingPattern(self):
        result = self.solution.longestCommonSubsequence("abab", "baba")
        self.assertEqual(result, 3)

    def testOneIsSubsequenceOfOther(self):
        result = self.solution.longestCommonSubsequence("ace", "abcde")
        self.assertEqual(result, 3)

    def testReverseStrings(self):
        result = self.solution.longestCommonSubsequence("abc", "cba")
        self.assertEqual(result, 1)

    def testLongerStringsWithPartialMatch(self):
        result = self.solution.longestCommonSubsequence("abcdefgh", "acdeh")
        self.assertEqual(result, 5)

    def testDifferentLengths(self):
        result = self.solution.longestCommonSubsequence("ab", "abcdefgh")
        self.assertEqual(result, 2)

    def testCommonPrefix(self):
        result = self.solution.longestCommonSubsequence("abcxyz", "abcdef")
        self.assertEqual(result, 3)

    def testCommonSuffix(self):
        result = self.solution.longestCommonSubsequence("xyzabc", "defabc")
        self.assertEqual(result, 3)

    def testInterleavedCharacters(self):
        result = self.solution.longestCommonSubsequence("abcde", "aec")
        self.assertEqual(result, 2)

    def testRepeatedPatternsInBoth(self):
        result = self.solution.longestCommonSubsequence("aaaa", "aaaa")
        self.assertEqual(result, 4)

    def testLongStringsNoCommon(self):
        result = self.solution.longestCommonSubsequence("abcdefghij", "klmnopqrst")
        self.assertEqual(result, 0)

    def testLongStringsWithCommon(self):
        result = self.solution.longestCommonSubsequence("abcdefghij", "acegikm")
        self.assertEqual(result, 5)

    def testCaseSensitivity(self):
        # Lowercase and uppercase are different
        result = self.solution.longestCommonSubsequence("abc", "ABC")
        self.assertEqual(result, 0)

    def testMixedCase(self):
        result = self.solution.longestCommonSubsequence("aBc", "abc")
        self.assertEqual(result, 2)

    def testComplexPattern1(self):
        result = self.solution.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy")
        self.assertEqual(result, 2)

    def testComplexPattern2(self):
        result = self.solution.longestCommonSubsequence("aggtab", "gxtxayb")
        self.assertEqual(result, 4)

    def testSingleCharacterInLongString(self):
        result = self.solution.longestCommonSubsequence("a", "abcdefghij")
        self.assertEqual(result, 1)

    def testAllSameCharacter(self):
        result = self.solution.longestCommonSubsequence("aaaa", "aa")
        self.assertEqual(result, 2)

    def testPartialOverlap(self):
        result = self.solution.longestCommonSubsequence("programming", "gaming")
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()