import unittest
from longest_substring_without_repeating_characters import Solution

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "abcabcbb"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

    def testAllUnique(self):
        s = "abcdef"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 6)

    def testAllSame(self):
        s = "bbbbb"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 1)

    def testEmptyString(self):
        s = ""
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 0)

    def testSingleCharacter(self):
        s = "a"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 1)

    def testLongestAtEnd(self):
        s = "abcabcdefgh"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 8)

    def testLongestAtBeginning(self):
        s = "pwwkew"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

    def testWithSpaces(self):
        s = "a b c a b c"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

    def testMixedCase(self):
        s = "dvdf"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

    def testSpecialCharacters(self):
        s = "!@#$%!@#"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 5)

    def testLongString(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 26)


if __name__ == '__main__':
    unittest.main()