import unittest
from string_compression import Solution


class TestCompress(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCompression(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "2", "b", "2", "c", "3"])

    def testLeetCodeExample1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "2", "b", "2", "c", "3"])

    def testLeetCodeExample2(self):
        chars = ["a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 1)
        self.assertEqual(chars[:result], ["a"])

    def testLeetCodeExample3(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["a", "b", "1", "2"])

    def testSingleCharacter(self):
        chars = ["a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 1)
        self.assertEqual(chars[:result], ["a"])

    def testTwoSameCharacters(self):
        chars = ["a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "2"])

    def testTwoDifferentCharacters(self):
        chars = ["a", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "b"])

    def testNoCompression(self):
        chars = ["a", "b", "c", "d", "e"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 5)
        self.assertEqual(chars[:result], ["a", "b", "c", "d", "e"])

    def testAllSameCharacter(self):
        chars = ["a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "5"])

    def testThreeRepeated(self):
        chars = ["a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "3"])

    def testAlternating(self):
        chars = ["a", "b", "a", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["a", "b", "a", "b"])

    def testDoubleDigitCount(self):
        chars = ["a"] * 10
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "1", "0"])

    def testTripleDigitCount(self):
        chars = ["a"] * 100
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["a", "1", "0", "0"])

    def testLargeCount(self):
        chars = ["a"] * 12
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "1", "2"])

    def testMixedCounts(self):
        chars = ["a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 5)
        self.assertEqual(chars[:result], ["a", "3", "b", "1", "2"])

    def testSingleThenMultiple(self):
        chars = ["a", "b", "b", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "b", "3"])

    def testMultipleThenSingle(self):
        chars = ["a", "a", "a", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "3", "b"])

    def testFourCharacters(self):
        chars = ["a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "4"])

    def testSixCharacters(self):
        chars = ["a", "a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "6"])

    def testSevenCharacters(self):
        chars = ["a", "a", "a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "7"])

    def testEightCharacters(self):
        chars = ["a", "a", "a", "a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "8"])

    def testNineCharacters(self):
        chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "9"])

    def testMultipleGroups(self):
        chars = ["a", "a", "b", "b", "c", "c"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "2", "b", "2", "c", "2"])

    def testThreeGroups(self):
        chars = ["a", "a", "a", "b", "b", "c"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 5)
        self.assertEqual(chars[:result], ["a", "3", "b", "2", "c"])

    def testFourGroups(self):
        chars = ["a", "a", "b", "c", "c", "d", "d", "d"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 7)
        self.assertEqual(chars[:result], ["a", "2", "b", "c", "2", "d", "3"])

    def testRepeatingPattern(self):
        chars = ["a", "a", "b", "b", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "2", "b", "2", "a", "2"])

    def testLongSequence(self):
        chars = ["a"] * 15 + ["b"] * 5
        result = self.solution.compress(chars)
        self.assertEqual(result, 5)
        self.assertEqual(chars[:result], ["a", "1", "5", "b", "5"])

    def testMixedLengths(self):
        chars = ["a", "b", "b", "c", "c", "c", "d", "d", "d", "d"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 7)
        self.assertEqual(chars[:result], ["a", "b", "2", "c", "3", "d", "4"])

    def testAllUnique(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "b", "c", "d", "e", "f"])

    def testTwoGroups(self):
        chars = ["a", "a", "a", "b", "b", "b", "b"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["a", "3", "b", "4"])

    def testUppercaseLetters(self):
        chars = ["A", "A", "A"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["A", "3"])

    def testMixedCase(self):
        chars = ["A", "A", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["A", "2", "a", "2"])

    def testVeryLongSequence(self):
        chars = ["a"] * 50
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "5", "0"])

    def testMaxDoubleDigit(self):
        chars = ["a"] * 99
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "9", "9"])

    def testMinTripleDigit(self):
        chars = ["a"] * 100
        result = self.solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:result], ["a", "1", "0", "0"])

    def testAlternatingPairs(self):
        chars = ["a", "a", "b", "b", "c", "c", "d", "d"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 8)
        self.assertEqual(chars[:result], ["a", "2", "b", "2", "c", "2", "d", "2"])

    def testSinglesBetweenGroups(self):
        chars = ["a", "a", "b", "c", "c", "d", "e", "e"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 8)
        self.assertEqual(chars[:result], ["a", "2", "b", "c", "2", "d", "e", "2"])

    def testLargeGroups(self):
        chars = ["a"] * 20 + ["b"] * 15 + ["c"] * 10
        result = self.solution.compress(chars)
        self.assertEqual(result, 9)
        self.assertEqual(chars[:result], ["a", "2", "0", "b", "1", "5", "c", "1", "0"])

    def testCount11(self):
        chars = ["a"] * 11
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "1", "1"])

    def testMultipleCount10(self):
        chars = ["a"] * 10 + ["b"] * 10
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "1", "0", "b", "1", "0"])

    def testComplexPattern(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:result], ["a", "b", "1", "2", "c", "3"])

    def testFiveCharSeq(self):
        chars = ["a", "a", "a", "a", "a"]
        result = self.solution.compress(chars)
        self.assertEqual(result, 2)
        self.assertEqual(chars[:result], ["a", "5"])

    def testSixteenCharSeq(self):
        chars = ["a"] * 16
        result = self.solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:result], ["a", "1", "6"])


if __name__ == '__main__':
    unittest.main()