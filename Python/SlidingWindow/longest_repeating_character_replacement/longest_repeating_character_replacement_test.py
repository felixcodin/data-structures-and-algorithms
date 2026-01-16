import unittest
from longest_repeating_character_replacement import Solution

class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicReplacement(self):
        s = "ABAB"
        k = 2
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 4)

    def testNoReplacement(self):
        s = "AAAAAA"
        k = 0
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 6)

    def testLongerString(self):
        s = "AABABBA"
        k = 1
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 4)

    def testSingleCharacter(self):
        s = "A"
        k = 1
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 1)

    def testMultipleReplacements(self):
        s = "ABCDE"
        k = 2
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 3)

    def testAllDifferent(self):
        s = "ABCD"
        k = 0
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 1)

    def testLargeK(self):
        s = "ABCD"
        k = 3
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 4)

    def testRepeatingPattern(self):
        s = "AAABBBCCC"
        k = 2
        res = self.solution.characterReplacement(s, k)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()