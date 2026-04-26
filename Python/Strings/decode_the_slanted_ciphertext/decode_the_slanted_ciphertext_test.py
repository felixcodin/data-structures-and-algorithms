import unittest

from decode_the_slanted_ciphertext import Solution


class TestDecodeTheSlantedCiphertext(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        encoded_text = "ch   ie   pr"
        rows = 3
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "cipher")

    def test_leetcode_example_2(self):
        encoded_text = "iveo    eed   l te   olc"
        rows = 4
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "i love leetcode")

    def test_leetcode_example_3_rows_one(self):
        encoded_text = "coding"
        rows = 1
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "coding")

    def test_empty_encoded_text(self):
        encoded_text = ""
        rows = 5
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "")

    def test_trailing_spaces_are_removed(self):
        encoded_text = "a   "
        rows = 2
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "a")

    def test_internal_spaces_are_preserved(self):
        encoded_text = "i love leetcode"
        rows = 1
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "i love leetcode")

    def test_single_column_matrix(self):
        encoded_text = "abc"
        rows = 3
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "ac")

    def test_rows_greater_than_length_current_behavior(self):
        encoded_text = "abc"
        rows = 5
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "")

    def test_all_spaces_decode_to_empty(self):
        encoded_text = "        "
        rows = 2
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "")

    def test_general_case_no_trailing_trim_needed(self):
        encoded_text = "abcdwxyz"
        rows = 2
        self.assertEqual(self.solution.decodeCiphertext(encoded_text, rows), "axbyczd")


if __name__ == "__main__":
    unittest.main()
