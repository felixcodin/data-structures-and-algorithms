import unittest
from reverse_vowels_of_a_string import Solution


class TestReverseVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "hello"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "holle")

    def testLeetCodeExample1(self):
        s = "hello"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "holle")

    def testLeetCodeExample2(self):
        s = "leetcode"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "leotcede")

    def testSingleVowel(self):
        s = "a"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "a")

    def testSingleConsonant(self):
        s = "b"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "b")

    def testNoVowels(self):
        s = "bcdfg"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "bcdfg")

    def testAllVowels(self):
        s = "aeiou"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "uoiea")

    def testAllVowelsUppercase(self):
        s = "AEIOU"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "UOIEA")

    def testMixedCase(self):
        s = "AeIoU"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "UoIeA")

    def testEmptyString(self):
        s = ""
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "")

    def testTwoVowels(self):
        s = "ai"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "ia")

    def testTwoVowelsSeparated(self):
        s = "race car"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "race car")

    def testVowelsAtEnds(self):
        s = "aibca"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "aibca")

    def testVowelsInMiddle(self):
        s = "baeicd"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "bieacd")

    def testMultipleVowels(self):
        s = "programming"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "prigrammong")

    def testOnlyConsonants(self):
        s = "xyz"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "xyz")

    def testRepeatedVowels(self):
        s = "aaa"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "aaa")

    def testAlternatingVowelsConsonants(self):
        s = "abacadae"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "ebacadaa")

    def testUppercaseVowels(self):
        s = "HELLO"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "HOLLE")

    def testMixedCaseVowels(self):
        s = "HeLLo"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "HoLLe")

    def testLongString(self):
        s = "aAbBcCdDeEfFgGhHiIjJ"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "IibBcCdDEefFgGhHAajJ")

    def testWithSpaces(self):
        s = "a e i o u"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "u o i e a")

    def testWithSpecialCharacters(self):
        s = "a!e@i#o$u"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "u!o@i#e$a")

    def testOnlySpaces(self):
        s = "   "
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "   ")

    def testSingleCharacterVowel(self):
        s = "E"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "E")

    def testTwoCharactersNoVowels(self):
        s = "bc"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "bc")

    def testTwoCharactersBothVowels(self):
        s = "ae"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "ea")

    def testThreeVowels(self):
        s = "aei"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "iea")

    def testFourVowels(self):
        s = "aeio"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "oiea")

    def testVowelAtStart(self):
        s = "apple"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "eppla")

    def testVowelAtEnd(self):
        s = "tree"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "tree")

    def testComplexString(self):
        s = "beautiful"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "buiutafel")

    def testPalindrome(self):
        s = "racecar"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "racecar")

    def testAllSameVowel(self):
        s = "eeee"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "eeee")

    def testMixedVowelsAndNumbers(self):
        s = "a1e2i3o4u5"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "u1o2i3e4a5")

    def testLongNoVowels(self):
        s = "bcdfghjklmnpqrstvwxyz"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "bcdfghjklmnpqrstvwxyz")

    def testAdjacentVowels(self):
        s = "aeiou"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "uoiea")

    def testYNotVowel(self):
        s = "yes"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "yes")

    def testCaseSensitivity(self):
        s = "AaBbCcDdEe"
        result = self.solution.reverseVowels(s)
        self.assertEqual(result, "eEBbCcDdaA")


if __name__ == '__main__':
    unittest.main()