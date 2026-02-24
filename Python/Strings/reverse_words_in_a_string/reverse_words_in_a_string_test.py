import unittest
from reverse_words_in_a_string import Solution


class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        s = "the sky is blue"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "blue is sky the")

    def testLeetCodeExample1(self):
        s = "the sky is blue"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "blue is sky the")

    def testLeetCodeExample2(self):
        s = "  hello world  "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testLeetCodeExample3(self):
        s = "a good   example"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "example good a")

    def testSingleWord(self):
        s = "hello"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "hello")

    def testSingleCharacter(self):
        s = "a"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "a")

    def testTwoWords(self):
        s = "hello world"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testLeadingSpaces(self):
        s = "   hello"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "hello")

    def testTrailingSpaces(self):
        s = "hello   "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "hello")

    def testLeadingAndTrailingSpaces(self):
        s = "   hello world   "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testMultipleSpacesBetweenWords(self):
        s = "hello    world"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testMultipleSpacesEverywhere(self):
        s = "  hello   world  "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testOnlySpaces(self):
        s = "     "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "")

    def testSingleSpace(self):
        s = " "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "")

    def testThreeWords(self):
        s = "one two three"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "three two one")

    def testFourWords(self):
        s = "a b c d"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "d c b a")

    def testWithPunctuation(self):
        s = "hello, world!"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world! hello,")

    def testWithNumbers(self):
        s = "123 456 789"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "789 456 123")

    def testMixedCaseWords(self):
        s = "Hello World"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "World Hello")

    def testAllUppercase(self):
        s = "HELLO WORLD"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "WORLD HELLO")

    def testAllLowercase(self):
        s = "hello world"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testSingleWordWithSpaces(self):
        s = "  hello  "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "hello")

    def testManyWords(self):
        s = "a b c d e f g"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "g f e d c b a")

    def testLongWords(self):
        s = "programming language python"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "python language programming")

    def testVeryLongString(self):
        s = "this is a very long string with many words in it"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "it in words many with string long very a is this")

    def testWithSpecialCharacters(self):
        s = "hello @world #test"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "#test @world hello")

    def testWithHyphens(self):
        s = "hello-world test-case"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "test-case hello-world")

    def testWithUnderscores(self):
        s = "hello_world test_case"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "test_case hello_world")

    def testAlphanumeric(self):
        s = "abc123 def456"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "def456 abc123")

    def testTwoWordsWithManySpaces(self):
        s = "hello          world"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testSentenceWithPunctuation(self):
        s = "Hello, how are you?"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "you? are how Hello,")

    def testNumbersAndLetters(self):
        s = "1a 2b 3c"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "3c 2b 1a")

    def testRepeatedWords(self):
        s = "hello hello world"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello hello")

    def testSingleLetterWords(self):
        s = "a b c"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "c b a")

    def testMixedSpacing(self):
        s = "  a   b    c  "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "c b a")

    def testComplexSpacing(self):
        s = "   the    quick   brown   fox   "
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "fox brown quick the")

    def testWordsWithDots(self):
        s = "hello.world test.case"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "test.case hello.world")

    def testTabsAsSpaces(self):
        s = "hello\tworld"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testNewlinesAsSpaces(self):
        s = "hello\nworld"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "world hello")

    def testMixedWhitespace(self):
        s = "hello \t world \n test"
        result = self.solution.reverseWords(s)
        self.assertEqual(result, "test world hello")


if __name__ == '__main__':
    unittest.main()