import unittest
from encode_and_decode_strings import Solution

class TestEncodeAndDecodeStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def testExampleCase(self):
        strs = ["we","say",":","yes","!@#$%^&*()"]
        strEncode = self.solution.encode(strs)
        res = self.solution.decode(strEncode)
        self.assertEqual(res, strs)
    def testEmptyStrings(self):
        strs = ["", "", ""]
        strEncode = self.solution.encode(strs)
        res = self.solution.decode(strEncode)
        self.assertEqual(res, strs)
    def testSingleCharacterStrings(self):
        strs = ["a", "b", "c"]
        strEncode = self.solution.encode(strs)
        res = self.solution.decode(strEncode)
        self.assertEqual(res, strs)
    def testLongStrings(self):
        strs = ["a" * 100, "b" * 200, "c" * 300]
        strEncode = self.solution.encode(strs)
        res = self.solution.decode(strEncode)
        self.assertEqual(res, strs)
    def testMixedCharacters(self):
        strs = ["abc123", "def!@#", "ghi%^&"]
        strEncode = self.solution.encode(strs)
        res = self.solution.decode(strEncode)
        self.assertEqual(res, strs)

if __name__ == '__main__':
    unittest.main()
