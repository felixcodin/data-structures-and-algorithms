import unittest
from count_of_substrings_containing_every_vowel_and_K_consonants_2 import Solution

class TestCountOfSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        word = "aeioqq"
        k = 1
        res = self.solution.countOfSubstrings(word, k)
        self.assertEqual(res, 0)

    def testStringOfAllVowels(self):
        word = "aeoui"
        k = 0
        res = self.solution.countOfSubstrings(word, k)
        self.assertEqual(res, 1)

    def testLargeString(self):
        word = "ieaouqqieaouqq"
        k = 1
        res = self.solution.countOfSubstrings(word, k)
        self.assertEqual(res, 3)

    def testWorseCase(self):
        word = "iqeaouqi"
        k = 2
        res = self.solution.countOfSubstrings(word, k)
        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()