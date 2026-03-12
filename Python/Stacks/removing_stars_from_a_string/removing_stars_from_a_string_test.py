import unittest
from removing_stars_from_a_string import Solution


class TestRemoveStars(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "leet**cod*e"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "lecoe")

    def testNoStars(self):
        s = "abc"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abc")

    def testEmptyString(self):
        s = ""
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testSingleCharacter(self):
        s = "a"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testSingleStar(self):
        s = "a*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testTwoCharactersOneStar(self):
        s = "ab*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testConsecutiveStars(self):
        s = "abc**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testThreeConsecutiveStars(self):
        s = "abcd***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testAllStarsRemoveAll(self):
        s = "abc***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testStarAtStart(self):
        s = "a*bc"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "bc")

    def testStarInMiddle(self):
        s = "ab*cd"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "acd")

    def testStarAtEnd(self):
        s = "abc*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testAlternatingStars(self):
        s = "a*b*c*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testAlternatingCharsStar(self):
        s = "ab*cd*ef*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ace")

    def testLongString(self):
        s = "abcdefgh*i*j*k*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcdefg")

    def testRepeatedCharacters(self):
        s = "aaa*a*a*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "aa")

    def testMixedPattern(self):
        s = "a*b*c*d"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "d")

    def testDoubleStarsInMiddle(self):
        s = "ab**cd"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "cd")

    def testTripleStarsInMiddle(self):
        s = "abc***def"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "def")

    def testComplexPattern1(self):
        s = "leet**cod*e"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "lecoe")

    def testComplexPattern2(self):
        s = "erase*****"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testComplexPattern3(self):
        s = "abb*cdfg*****x*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testAllCharactersRemoved(self):
        s = "a*b*c*d*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testSomeCharactersRemain(self):
        s = "abc*de*f"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abdf")

    def testStarsRemovingFromEnd(self):
        s = "abcdef***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abc")

    def testStarsRemovingFromMiddle(self):
        s = "abc**def"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "adef")

    def testTwoCharsTwoStars(self):
        s = "ab**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testThreeCharsThreeStars(self):
        s = "abc***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testFourCharsTwoStars(self):
        s = "abcd**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testEvenDistribution(self):
        s = "a*b*c*d*e*f*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testUnevenDistribution(self):
        s = "ab*cd*ef*gh"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "acegh")

    def testThreeInARow(self):
        s = "abc***d"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "d")

    def testLongNoStars(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcdefghijklmnopqrstuvwxyz")

    def testLongWithStars(self):
        s = "abcdefghijklmnopqrstuvwxyz" + "*" * 26
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testPartialRemoval(self):
        s = "hello*world"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "hellworld")

    def testMultipleWords(self):
        s = "hello* *world*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "hellworl")

    def testRepeatedPattern(self):
        s = "ab*ab*ab*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "aaa")

    def testIncreasingStars(self):
        s = "a*bc**def***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testDecreasingStars(self):
        s = "abc***de**f*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testDigitsAndStars(self):
        s = "123*45*6*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "124")

    def testSpecialCharsAndStars(self):
        s = "a!b*c#*d$*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a!cd")

    def testSpacesAndStars(self):
        s = "a b*c *d*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a c")

    def testAlphanumeric(self):
        s = "a1b2*c3*d4*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a1bcd")

    def testSingleStarAtEnd(self):
        s = "test*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "tes")

    def testSingleStarInMiddle(self):
        s = "te*st"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "tst")

    def testManySmallSegments(self):
        s = "a*b*c*d*e*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testZigzagPattern(self):
        s = "ab*cd*ef*gh"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "acegh")

    def testBlockPattern(self):
        s = "aaaa****bbbb"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "bbbb")

    def testEmptyAfterRemoval(self):
        s = "x*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testTwoSegments(self):
        s = "abc***xyz"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "xyz")

    def testThreeSegments(self):
        s = "abc**def**ghi"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "adghi")

    def testFourSegments(self):
        s = "ab*cd*ef*gh*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "aceg")

    def testStarRemovesLastChar(self):
        s = "programming*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "programmin")

    def testMultipleStarsRemoveLast(self):
        s = "programming***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "programm")

    def testAllButOneRemoved(self):
        s = "abc**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a")

    def testExactlyHalfRemoved(self):
        s = "abcd**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testMoreThanHalfRemoved(self):
        s = "abcde***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testLessThanHalfRemoved(self):
        s = "abcdef**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcd")

    def testAlternatingMany(self):
        s = "a*b*c*d*e*f*g*h*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testGroupedStars(self):
        s = "abc***def***ghi"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ghi")

    def testScatteredStars(self):
        s = "a*bc*de*fg*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "bdf")

    def testVeryLongString(self):
        s = "a" * 100 + "*" * 50
        result = self.solution.removeStars(s)
        self.assertEqual(result, "a" * 50)

    def testVeryLongAllRemoved(self):
        s = "a" * 100 + "*" * 100
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testComplexRealWorld(self):
        s = "hello*world**test***"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "hellwort")

    def testEdgeCase1(self):
        s = "*a"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "*a")

    def testEdgeCase3(self):
        s = "a*b"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "b")

    def testEdgeCase4(self):
        s = "ab*c"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ac")

    def testSymmetric(self):
        s = "abc*def*ghi"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abdeghi")

    def testAsymmetric(self):
        s = "abcdef***ghi"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcghi")

    def testCascadingRemoval(self):
        s = "abcdefgh********"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testPartialCascade(self):
        s = "abcdefgh****"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcd")

    def testInterleavedPattern(self):
        s = "a*b*c*defg"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "defg")

    def testDoubleAlternating(self):
        s = "aa**bb**cc**"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testTripleAlternating(self):
        s = "aaa***bbb***ccc"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ccc")

    def testFrontHeavy(self):
        s = "aaaaa*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "aaaa")

    def testMiddleHeavy(self):
        s = "aa**bb"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "bb")

    def testUnbalanced(self):
        s = "aaaaaaa*b"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "aaaaaab")

    def testBalanced(self):
        s = "aaaa****bbbb"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "bbbb")

    def testSingleCharRemoval(self):
        s = "abcdefg*hijklmn"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abcdefhijklmn")

    def testMultiCharRemoval(self):
        s = "abcdefg****hijklmn"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abchijklmn")

    def testPalindromicInput(self):
        s = "aba*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testNonPalindromicInput(self):
        s = "abc*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "ab")

    def testRepeatingSubstring(self):
        s = "abab*abab*"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "abaaba")

    def testNoChangeNeeded(self):
        s = "unchanged"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "unchanged")

    def testCompleteRemoval(self):
        s = "remove******"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")

    def testMinimalInput(self):
        s = "a*b"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "b")

    def testLastExample(self):
        s = "erase*****"
        result = self.solution.removeStars(s)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()