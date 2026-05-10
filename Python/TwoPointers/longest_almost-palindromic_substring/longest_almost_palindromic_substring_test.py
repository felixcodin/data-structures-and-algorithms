import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("longest_almost_palindromic_substring.py")
spec = importlib.util.spec_from_file_location("longest_almost_palindromic_substring", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLongestAlmostPalindromicSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_empty_string(self) -> None:
        self.assertEqual(self.solution.almostPalindromic(""), 0)

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("a"), 1)

    def test_two_different_characters(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("ab"), 2)

    def test_odd_palindrome(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("aba"), 3)

    def test_even_palindrome(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("abba"), 4)

    def test_almost_palindrome_with_one_inner_mismatch(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("abca"), 4)

    def test_no_longer_palindrome_than_two(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("abcdef"), 2)

    def test_leetcode_style_mixed_case(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("abc"), 2)

    def test_full_length_result(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("aaabaaa"), 7)

    def test_odd_length_complete_match(self) -> None:
        self.assertEqual(self.solution.almostPalindromic("baaab"), 5)


if __name__ == "__main__":
    unittest.main()
