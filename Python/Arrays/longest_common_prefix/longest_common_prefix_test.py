import unittest
from longest_common_prefix import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testCommonPrefix(self):
        strs = ["flower", "flow", "flight"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "fl")

    def testNoCommonPrefix(self):
        strs = ["dog", "racecar", "car"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "")

    def testSingleString(self):
        strs = ["alone"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "alone")

    def testEmptyArray(self):
        strs = []
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "")

    def testIdenticalStrings(self):
        strs = ["test", "test", "test"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "test")

    def testOneEmptyString(self):
        strs = ["", "b"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "")

    def testDifferentLengths(self):
        strs = ["ab", "a"]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "a")

    def testAllEmpty(self):
        strs = ["", "", ""]
        res = self.solution.longestCommonPrefix(strs)
        self.assertEqual(res, "")


if __name__ == '__main__':
    unittest.main()