import unittest
from longest_palindromic_substring import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleCharacter(self):
        s = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "a")

    def testTwoSameCharacters(self):
        s = "aa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aa")

    def testOddLengthPalindrome(self):
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])

    def testEvenLengthPalindrome(self):
        s = "cbbd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bb")

    def testEntireStringPalindrome(self):
        s = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "racecar")

    def testNoPalindrome(self):
        s = "abcdef"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 1)

    def testMultipleSameCharacters(self):
        s = "aaaa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aaaa")

    def testPalindromeAtEnd(self):
        s = "abcdd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "dd")

    def testPalindromeAtStart(self):
        s = "bbbbabc"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bbbb")

    def testLongString(self):
        s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendure"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["ranynar", "rtsestr"])

    def testMixedPalindromes(self):
        s = "bananas"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "anana")


if __name__ == '__main__':
    unittest.main()