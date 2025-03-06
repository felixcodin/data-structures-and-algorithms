import unittest
from group_anagrams import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def testExampleCase(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res = self.solution.groupAnagrams(strs)
        self.assertEqual(res, [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    def testSingleString(self):
        strs = ["x"]
        res = self.solution.groupAnagrams(strs)
        self.assertEqual(res, [["x"]])
    def testEmptyString(self):
        strs = [""]
        res = self.solution.groupAnagrams(strs)
        self.assertEqual(res, [[""]])

if __name__ == '__main__':
    unittest.main()