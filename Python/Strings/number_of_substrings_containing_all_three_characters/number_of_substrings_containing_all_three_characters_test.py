import unittest
from number_of_substrings_containing_all_three_characters import Solution

class TestNumberOfSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        s = "abcabc"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 10)
    
    def testEasyCase(self):
        s = "abc"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 1)

    def testStringWithoutThreeCharacters(self):
        s = "aabb"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 0)

    def testEmptyString(self):
        s = ""
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 0)

    def testStringWithOneCharacter(self):
        s = "aaa"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 0)

    def testStringWithRepeatCharaters(self):
        s = "aaabbbccc"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 9)

    def testLongAndComplexString(self):
        s = "abcabcabcabc"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 55)

    def testNonConsecutiveCharaters(self):
        s = "abacbc"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 8)

    def testTwoCharactersString(self):
        s = "aabb"
        res = self.solution.numberOfSubstrings(s)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()