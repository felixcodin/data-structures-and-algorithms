import unittest
from greatest_common_divisor_of_strings import Solution


class TestGcdOfStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCommonDivisor(self):
        str1 = "ABCABC"
        str2 = "ABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "ABC")

    def testLongerCommonDivisor(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "AB")

    def testNoCommonDivisor(self):
        str1 = "ABCDEF"
        str2 = "ABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "")

    def testEqualStrings(self):
        str1 = "ABC"
        str2 = "ABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "ABC")

    def testSingleCharacter(self):
        str1 = "AAA"
        str2 = "A"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "A")

    def testSingleCharacterBoth(self):
        str1 = "A"
        str2 = "A"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "A")

    def testEmptyFirstString(self):
        str1 = ""
        str2 = "ABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "")

    def testBothEmptyStrings(self):
        str1 = ""
        str2 = ""
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "")

    def testLeetCodeExample1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "ABC")

    def testLeetCodeExample2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "AB")

    def testLeetCodeExample3(self):
        str1 = "LEET"
        str2 = "CODE"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "")

    def testMultipleRepeatedPattern(self):
        str1 = "ABABABAB"
        str2 = "ABAB"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "ABAB")

    def testLongerFirstString(self):
        str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "TAUXX")

    def testDifferentPatterns(self):
        str1 = "ABCABCABC"
        str2 = "ABCABC"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "ABC")

    def testNonDivisiblePattern(self):
        str1 = "ABCDEF"
        str2 = "XYZ"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "")

    def testSameRepeatedChar(self):
        str1 = "AAAAAA"
        str2 = "AAA"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "AAA")

    def testTwoCharPattern(self):
        str1 = "XYXYXY"
        str2 = "XY"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "XY")

    def testPrimeGcd(self):
        str1 = "ABABABABAB"
        str2 = "ABABABABABABABAB"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "AB")

    def testStr2LongerThanStr1(self):
        str1 = "AB"
        str2 = "ABAB"
        result = self.solution.gcdOfStrings(str1, str2)
        self.assertEqual(result, "AB")


if __name__ == '__main__':
    unittest.main()