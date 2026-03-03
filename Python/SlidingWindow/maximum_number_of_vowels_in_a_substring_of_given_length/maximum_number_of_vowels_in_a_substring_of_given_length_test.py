import unittest
from maximum_number_of_vowels_in_a_substring_of_given_length import Solution


class TestMaxVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "abciiidef"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testLeetCodeExample1(self):
        s = "abciiidef"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testLeetCodeExample2(self):
        s = "aeiou"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testLeetCodeExample3(self):
        s = "leetcode"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testSingleCharacterVowel(self):
        s = "a"
        k = 1
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testSingleCharacterConsonant(self):
        s = "b"
        k = 1
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testAllVowels(self):
        s = "aeiou"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testAllConsonants(self):
        s = "bcdfg"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testKEqualsOne(self):
        s = "abcde"
        k = 1
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testKEqualsStringLength(self):
        s = "aeiou"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testNoVowelsInString(self):
        s = "bcdfghjklmnpqrstvwxyz"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testMaxAtStart(self):
        s = "aeiobcd"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 4)

    def testMaxAtEnd(self):
        s = "bcdeaeiou"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testMaxInMiddle(self):
        s = "bcaeioufgh"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testTwoCharacters(self):
        s = "ae"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testTwoVowelsTwoConsonants(self):
        s = "aebc"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testAlternatingVowelsConsonants(self):
        s = "ababab"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testRepeatedVowel(self):
        s = "aaaa"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testRepeatedConsonant(self):
        s = "bbbb"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testOneVowelManyConsonants(self):
        s = "abcdefg"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testManyVowelsOneConsonant(self):
        s = "aeioub"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testSmallK(self):
        s = "aeiouaeiou"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testLargeK(self):
        s = "aeiouaeiou"
        k = 8
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 8)

    def testConsecutiveVowels(self):
        s = "aaaaa"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testScatteredVowels(self):
        s = "abacadaea"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testAllFiveVowels(self):
        s = "aeiou"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testAllFiveVowelsMixed(self):
        s = "aeiouaeiou"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testLongStringAllConsonants(self):
        s = "bcdfghjklmnpqrstvwxyz"
        k = 10
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testLongStringAllVowels(self):
        s = "aeiouaeiouaeiou"
        k = 10
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 10)

    def testSlidingWindowEffect(self):
        s = "weallloveyou"
        k = 7
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 4)

    def testThreeCharWindow(self):
        s = "aeiou"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testFourCharWindow(self):
        s = "aeiou"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 4)

    def testVowelAtStartOnly(self):
        s = "abcdefg"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testVowelAtEndOnly(self):
        s = "bcdefga"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testMultipleWindowsSameCount(self):
        s = "abaaba"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testTwoVowelsInWindow(self):
        s = "aebcd"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testOneVowelInWindow(self):
        s = "abcde"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testZeroVowelsInWindow(self):
        s = "bcdfg"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 0)

    def testLongString(self):
        s = "a" * 100 + "b" * 100
        k = 50
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 50)

    def testPatternAEIOU(self):
        s = "aeiouaeiou"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testPatternWithConsonants(self):
        s = "abebiou"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testOnlyA(self):
        s = "aaaaa"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testOnlyE(self):
        s = "eeeee"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testOnlyI(self):
        s = "iiiii"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testOnlyO(self):
        s = "ooooo"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testOnlyU(self):
        s = "uuuuu"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testMixedVowelsAndB(self):
        s = "ababababab"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testVowelsGrouped(self):
        s = "aaabbbccc"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testVowelsAtBoundaries(self):
        s = "abcda"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testComplexPattern(self):
        s = "tryhard"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testRealWord(self):
        s = "programming"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testAnotherRealWord(self):
        s = "beautiful"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 4)

    def testKEqualTwo(self):
        s = "aeiou"
        k = 2
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)

    def testThreeConsecutiveVowels(self):
        s = "aaabbb"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 3)

    def testFourConsecutiveVowels(self):
        s = "aaaabbbb"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 4)

    def testFiveConsecutiveVowels(self):
        s = "aaaaabbbbb"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 5)

    def testSixCharString(self):
        s = "abcdef"
        k = 3
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testSevenCharString(self):
        s = "abcdefg"
        k = 4
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 1)

    def testEightCharString(self):
        s = "abcdefgh"
        k = 5
        result = self.solution.maxVowels(s, k)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()