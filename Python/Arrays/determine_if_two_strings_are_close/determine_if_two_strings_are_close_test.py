import unittest
from determine_if_two_strings_are_close import Solution


class TestCloseStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicClose(self):
        word1 = "abc"
        word2 = "bca"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testLeetCodeExample1(self):
        word1 = "abc"
        word2 = "bca"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        word1 = "a"
        word2 = "aa"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testLeetCodeExample3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testNotClose(self):
        word1 = "abc"
        word2 = "def"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testDifferentLengths(self):
        word1 = "abc"
        word2 = "abcd"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testEmptyStrings(self):
        word1 = ""
        word2 = ""
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testOneEmpty(self):
        word1 = "abc"
        word2 = ""
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSingleCharSame(self):
        word1 = "a"
        word2 = "a"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSingleCharDifferent(self):
        word1 = "a"
        word2 = "b"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testIdenticalStrings(self):
        word1 = "hello"
        word2 = "hello"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testAllSameCharacter(self):
        word1 = "aaaa"
        word2 = "aaaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testDifferentCharSets(self):
        word1 = "abc"
        word2 = "xyz"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSubsetCharSet(self):
        word1 = "aab"
        word2 = "abb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSameFrequencies(self):
        word1 = "aabbcc"
        word2 = "ccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testDifferentFrequencies(self):
        word1 = "aabbc"
        word2 = "abbcc"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSwapCharacters(self):
        word1 = "ab"
        word2 = "ba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testTransformCharacters(self):
        word1 = "aaa"
        word2 = "bbb"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testTransformAndSwap(self):
        word1 = "aabbcc"
        word2 = "ccaabb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testTwoCharacters(self):
        word1 = "aabb"
        word2 = "bbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testThreeCharacters(self):
        word1 = "aabbcc"
        word2 = "abcabc"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testMissingCharacter(self):
        word1 = "abc"
        word2 = "abd"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testExtraCharacter(self):
        word1 = "aab"
        word2 = "abc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testFrequencyPattern123(self):
        word1 = "abbccc"
        word2 = "cccbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testFrequencyPattern132(self):
        word1 = "abbccc"
        word2 = "accbbb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testFrequencyPattern111(self):
        word1 = "abc"
        word2 = "def"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testFrequencyPattern222(self):
        word1 = "aabbcc"
        word2 = "xxyyzz"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSameCharsNoClose(self):
        word1 = "aab"
        word2 = "aba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testLongStrings(self):
        word1 = "a" * 100 + "b" * 200
        word2 = "b" * 100 + "a" * 200
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testManyDuplicates(self):
        word1 = "aaabbbccc"
        word2 = "cccbbbaaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testAlphabet(self):
        word1 = "abcdefghijklmnopqrstuvwxyz"
        word2 = "zyxwvutsrqponmlkjihgfedcba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testPartialAlphabet(self):
        word1 = "abcde"
        word2 = "fghij"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testRepeatedPattern(self):
        word1 = "ababab"
        word2 = "bababa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testAlternatingPattern(self):
        word1 = "ababab"
        word2 = "aabbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testUnequalFrequencies(self):
        word1 = "aabbb"
        word2 = "abbbb"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testComplexPattern1(self):
        word1 = "uau"
        word2 = "ssx"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testComplexPattern2(self):
        word1 = "abbzzca"
        word2 = "babzzcz"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testComplexPattern3(self):
        word1 = "cabbba"
        word2 = "abbccc"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testFourCharacters(self):
        word1 = "aabbccdd"
        word2 = "ddccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testFiveCharacters(self):
        word1 = "aabbccdde"
        word2 = "eeddccbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSixCharacters(self):
        word1 = "aabbccddee"
        word2 = "eeddccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testMixedFrequencies1(self):
        word1 = "aaabbc"
        word2 = "ccbbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testMixedFrequencies2(self):
        word1 = "aaabbbc"
        word2 = "cccbbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSingleCharRepeated(self):
        word1 = "aaaa"
        word2 = "bbbb"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testTwoCharRepeated(self):
        word1 = "aabb"
        word2 = "ccdd"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSameCharsCloseFreq(self):
        word1 = "aaabbb"
        word2 = "bbbaaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testDifferentFreqSameChars(self):
        word1 = "aabbb"
        word2 = "aaabb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testOneCharExcessive(self):
        word1 = "aaaaab"
        word2 = "bbbbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testBalancedFrequencies(self):
        word1 = "aabbccdd"
        word2 = "abcdabcd"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testUnbalancedFrequencies(self):
        word1 = "aaaabbcd"
        word2 = "abcddddb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testPalindrome(self):
        word1 = "abcba"
        word2 = "bacab"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testNonPalindrome(self):
        word1 = "abcde"
        word2 = "edcba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testThreeElementsClose(self):
        word1 = "abc"
        word2 = "cab"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testThreeElementsNotClose(self):
        word1 = "abc"
        word2 = "xyz"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSymmetricFrequencies(self):
        word1 = "aabbcc"
        word2 = "ccaabb"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testAsymmetricFrequencies(self):
        word1 = "aaabbc"
        word2 = "cbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testVeryLongSame(self):
        word1 = "a" * 1000
        word2 = "a" * 1000
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testVeryLongDifferent(self):
        word1 = "a" * 1000
        word2 = "b" * 1000
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testMultipleTransformations(self):
        word1 = "aabbccddee"
        word2 = "eeddccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testNoTransformationNeeded(self):
        word1 = "test"
        word2 = "test"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testFrequency1234(self):
        word1 = "abbcccddddeeeee"
        word2 = "eeeeedddddcccbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testFrequency12345(self):
        word1 = "abbcccddddeeeeef"
        word2 = "feeeeeddddcccbba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testCharacterSubset(self):
        word1 = "aabbcc"
        word2 = "aabbc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testCharacterSuperset(self):
        word1 = "aabbc"
        word2 = "aabbcc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testDisjointCharSets(self):
        word1 = "abc"
        word2 = "def"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testOverlappingCharSets(self):
        word1 = "abcd"
        word2 = "cdef"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testMinimalOverlap(self):
        word1 = "abc"
        word2 = "axy"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testMaximalOverlap(self):
        word1 = "abc"
        word2 = "bca"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testSingleFrequencyDifference(self):
        word1 = "aaabbb"
        word2 = "aabbbb"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testDoubleFrequencyDifference(self):
        word1 = "aabbcc"
        word2 = "aaabbc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testSameFrequencyDistribution(self):
        word1 = "aabbcc"
        word2 = "ddeeff"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testDifferentFrequencyDistribution(self):
        word1 = "aabbcc"
        word2 = "aaabbc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testAllUniqueChars(self):
        word1 = "abcdef"
        word2 = "fedcba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testAllUniqueCharsDifferent(self):
        word1 = "abcdef"
        word2 = "ghijkl"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testRepeatingSubstring(self):
        word1 = "abcabc"
        word2 = "cbacba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testNonRepeatingSubstring(self):
        word1 = "abcdef"
        word2 = "defabc"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testComplexCase1(self):
        word1 = "abbzzcca"
        word2 = "babzzcaz"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testComplexCase2(self):
        word1 = "abbzzca"
        word2 = "babzzc"
        result = self.solution.closeStrings(word1, word2)
        self.assertFalse(result)

    def testComplexCase3(self):
        word1 = "aabbccddeeff"
        word2 = "ffeeddccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testZigZagPattern(self):
        word1 = "ababab"
        word2 = "bababa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testBlockPattern(self):
        word1 = "aaabbb"
        word2 = "bbbaaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testMixedPattern(self):
        word1 = "aabbaabb"
        word2 = "bbaabbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testConsecutiveChars(self):
        word1 = "abcdef"
        word2 = "fedcba"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testNonConsecutiveChars(self):
        word1 = "acehjl"
        word2 = "ljheca"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testLowercaseOnly(self):
        word1 = "hello"
        word2 = "olleh"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)

    def testLastExample(self):
        word1 = "aabbcc"
        word2 = "ccbbaa"
        result = self.solution.closeStrings(word1, word2)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()