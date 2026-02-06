import unittest
from palindromic_substring import Solution

class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleCharacter(self):
        s = "a"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 1)

    def testTwoSameCharacters(self):
        s = "aa"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 3)

    def testTwoDifferentCharacters(self):
        s = "ab"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 2)

    def testSimplePalindrome(self):
        s = "abc"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 3)

    def testAllSameCharacters(self):
        s = "aaaa"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 10)

    def testMixedString(self):
        s = "abba"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 6)

    def testPalindrome(self):
        s = "racecar"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 10)

    def testMultipleConsecutiveSameChars(self):
        s = "aabaa"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 9)

    def testEmptyLikeString(self):
        s = "a"
        result = self.solution.countSubstrings(s)
        self.assertGreater(result, 0)

    def testLongerString(self):
        s = "abacabad"
        result = self.solution.countSubstrings(s)
        self.assertGreater(result, 8)


if __name__ == '__main__':
    unittest.main()