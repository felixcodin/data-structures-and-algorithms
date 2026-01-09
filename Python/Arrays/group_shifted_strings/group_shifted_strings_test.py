import unittest
from group_shifted_strings import Solution

class TestGroupShiftedStrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        result = self.solution.groupStrings(strings)
        expected = [["abc", "bcd", "xyz"], ["acef"], ["az", "ba"], ["a", "z"]]
        self.assertEqual(sorted([sorted(group) for group in result]), 
                        sorted([sorted(group) for group in expected]))

    def testSingleString(self):
        strings = ["abc"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(result, [["abc"]])

    def testEmptyInput(self):
        strings = []
        result = self.solution.groupStrings(strings)
        self.assertEqual(result, [])

    def testSingleCharacters(self):
        strings = ["a", "b", "c"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), ["a", "b", "c"])

    def testSameStrings(self):
        strings = ["abc", "abc", "abc"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(result, [["abc", "abc", "abc"]])

    def testDifferentLengths(self):
        strings = ["a", "ab", "abc"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(len(result), 3)

    def testWrapAround(self):
        strings = ["az", "ba"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), ["az", "ba"])

    def testNoShift(self):
        strings = ["abc", "def", "ghi"]
        result = self.solution.groupStrings(strings)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), ["abc", "def", "ghi"])


if __name__ == '__main__':
    unittest.main()