import unittest
from roman_to_integer import Solution

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        s = "III"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 3)

    def testLargeCase(self):
        s = "MCMXCIV"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 1994)
    
    def testSingleRomanCase(self):
        s = "M"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 1000)

    def testCommonCase(self):
        s = "XX"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 20)

    def testSubtractionCase(self):
        s = "CMM"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 1900)

    def testComplexCase(self):
        s = "MMMCMXCIX"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 3999)

    def testEdgeCase(self):
        s = "MMM"
        res = self.solution.romanToInt(s)
        self.assertEqual(res, 3000)

if __name__ == '__main__':
    unittest.main()