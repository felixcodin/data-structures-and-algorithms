import unittest
from decode_string import Solution

class TestDecodeString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSimpleCase(self):
        s = "3[a]2[bc]"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "aaabcbc")

    def testNestedCase(self):
        s = "3[a2[c]]"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "accaccacc")

    def testMultipleDigits(self):
        s = "2[abc]3[cd]ef"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "abcabccdcdcdef")

    def testNoEncoding(self):
        s = "abcd"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "abcd")

    def testLargeNumber(self):
        s = "10[a]"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "aaaaaaaaaa")

    def testDeepNesting(self):
        s = "2[a2[b2[c]]]"
        res = self.solution.decodeString(s)
        self.assertEqual(res, "abccbccabccbcc")


if __name__ == '__main__':
    unittest.main()