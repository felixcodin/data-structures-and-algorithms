import unittest
from permutation_in_string import Solution


class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLeetCodeExample1(self):
        # "ab" has permutation "ba" in "eidbaooo"
        result = self.solution.checkInclusion("ab", "eidbaooo")
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        # "ab" has no permutation in "eidboaoo"
        result = self.solution.checkInclusion("ab", "eidboaoo")
        self.assertFalse(result)

    def testS2ShorterThanS1(self):
        result = self.solution.checkInclusion("abcd", "ab")
        self.assertFalse(result)

    def testExactMatchAtBeginning(self):
        result = self.solution.checkInclusion("abc", "abcdef")
        self.assertTrue(result)

    def testExactMatchAtEnd(self):
        result = self.solution.checkInclusion("abc", "xyzabc")
        self.assertTrue(result)

    def testExactMatchInMiddle(self):
        result = self.solution.checkInclusion("abc", "xyzabcdef")
        self.assertTrue(result)

    def testPermutationAtBeginning(self):
        result = self.solution.checkInclusion("abc", "bacdef")
        self.assertTrue(result)

    def testPermutationAtEnd(self):
        result = self.solution.checkInclusion("abc", "xyzcba")
        self.assertTrue(result)

    def testPermutationInMiddle(self):
        result = self.solution.checkInclusion("abc", "xyzcabdef")
        self.assertTrue(result)

    def testNoPermutationExists(self):
        result = self.solution.checkInclusion("abc", "defgh")
        self.assertFalse(result)

    def testSingleCharacterMatch(self):
        result = self.solution.checkInclusion("a", "abc")
        self.assertTrue(result)

    def testSingleCharacterNoMatch(self):
        result = self.solution.checkInclusion("a", "bcd")
        self.assertFalse(result)

    def testBothSingleCharacterMatch(self):
        result = self.solution.checkInclusion("a", "a")
        self.assertTrue(result)

    def testBothSingleCharacterNoMatch(self):
        result = self.solution.checkInclusion("a", "b")
        self.assertFalse(result)

    def testEqualStrings(self):
        result = self.solution.checkInclusion("abc", "abc")
        self.assertTrue(result)

    def testRepeatedCharactersInS1(self):
        result = self.solution.checkInclusion("aab", "xyzbaadef")
        self.assertTrue(result)

    def testRepeatedCharactersNoMatch(self):
        result = self.solution.checkInclusion("aaa", "aabaaa")
        self.assertTrue(result)

    def testAllSameCharactersMatch(self):
        result = self.solution.checkInclusion("aa", "aaaa")
        self.assertTrue(result)

    def testAllSameCharactersNoMatch(self):
        result = self.solution.checkInclusion("aaa", "aa")
        self.assertFalse(result)

    def testMultiplePotentialWindows(self):
        result = self.solution.checkInclusion("ab", "abaababbaba")
        self.assertTrue(result)

    def testPartialMatchNotEnough(self):
        result = self.solution.checkInclusion("abc", "aabbcc")
        self.assertFalse(result)

    def testLongerS1(self):
        result = self.solution.checkInclusion("hello", "ooolleooolleh")
        self.assertTrue(result)

    def testPermutationWithGap(self):
        result = self.solution.checkInclusion("ab", "axb")
        self.assertFalse(result)

    def testCharacterFrequencyMismatch(self):
        result = self.solution.checkInclusion("aab", "aaab")
        self.assertTrue(result)

    def testWindowAtVeryEnd(self):
        result = self.solution.checkInclusion("ab", "xyzba")
        self.assertTrue(result)

    def testComplexPermutation1(self):
        result = self.solution.checkInclusion("abc", "ccccbbbbaaaa")
        self.assertFalse(result)

    def testComplexPermutation2(self):
        result = self.solution.checkInclusion("abc", "bbbca")
        self.assertTrue(result)

    def testLongStringsWithPermutation(self):
        result = self.solution.checkInclusion("abcd", "xyzdcbaqwerty")
        self.assertTrue(result)

    def testLongStringsNoPermutation(self):
        result = self.solution.checkInclusion("abcd", "xyzabcqwerty")
        self.assertFalse(result)

    def testRepeatedPatternInS2(self):
        result = self.solution.checkInclusion("ab", "ababab")
        self.assertTrue(result)

    def testEmptyS1EdgeCase(self):
        # Note: based on problem constraints, s1.length >= 1
        # This is more of a defensive test
        result = self.solution.checkInclusion("", "abc")
        self.assertTrue(result)  # Empty string is trivially a permutation

    def testAllDifferentCharacters(self):
        result = self.solution.checkInclusion("abc", "defabc")
        self.assertTrue(result)

    def testInterleaved(self):
        result = self.solution.checkInclusion("abc", "axbycz")
        self.assertFalse(result)

    def testDuplicatesInBoth(self):
        result = self.solution.checkInclusion("aab", "baaxy")
        self.assertTrue(result)

    def testFrequencyExactMatch(self):
        result = self.solution.checkInclusion("aabc", "ahbgdcacabc")
        self.assertTrue(result)

    def testConsecutiveWindow(self):
        result = self.solution.checkInclusion("ab", "aeidbaooo")
        self.assertTrue(result)

    def testPermutationAtSecondPosition(self):
        result = self.solution.checkInclusion("ab", "xba")
        self.assertTrue(result)

    def testTwoCharacterPermutation(self):
        result = self.solution.checkInclusion("xy", "yx")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()