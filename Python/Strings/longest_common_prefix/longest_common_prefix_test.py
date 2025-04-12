import unittest
from longest_common_prefix import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        strs = ["flower","flow","flight"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "fl")

    def testCommonPrefixIsFullString(self):
        strs = ["dog", "dog", "dog"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "dog")

    def testNoCommonPrefix(self):
        strs = ["dog","racecar","car"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "")

    def testOneStringIsEmpty(self):
        strs = ["abc", ""]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "")

    def testAllStringAreEmpty(self):
        strs = ["", "", ""]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "")
    
    def testOnlyOneString(self):
        strs = ["wonderful"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "wonderful")

    def testOneStringIsPrefixOfTheOthers(self):
        strs = ["interspecies", "interstellar", "interstate"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "inters")

    def testLongStringsWithDeepCommonPrefix(self):
        strs = ["abcdefghijklmno", "abcdefghixyz", "abcdefghi"]
        sol = self.solution.longestCommonPrefix(strs)
        self.assertEqual(sol, "abcdefghi")

if __name__ == '__main__':
    unittest.main()