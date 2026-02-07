import unittest
from decode_ways import Solution

class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_digit(self):
        result = self.solution.numDecodings("1")
        self.assertEqual(result, 1)

    def test_two_digits_valid(self):
        result = self.solution.numDecodings("12")
        self.assertEqual(result, 2)

    def test_two_digits_invalid(self):
        result = self.solution.numDecodings("10")
        self.assertEqual(result, 1)

    def test_zero_at_start(self):
        result = self.solution.numDecodings("01")
        self.assertEqual(result, 0)

    def test_multiple_zeros(self):
        result = self.solution.numDecodings("100")
        self.assertEqual(result, 0)

    def test_valid_sequence(self):
        result = self.solution.numDecodings("226")
        self.assertEqual(result, 3)

    def test_zero_in_middle(self):
        result = self.solution.numDecodings("206")
        self.assertEqual(result, 1)

    def test_all_ones(self):
        result = self.solution.numDecodings("111")
        self.assertEqual(result, 3)

    def test_two_six(self):
        result = self.solution.numDecodings("26")
        self.assertEqual(result, 2)

    def test_twenty_six(self):
        result = self.solution.numDecodings("27")
        self.assertEqual(result, 1)

    def test_longer_sequence(self):
        result = self.solution.numDecodings("2626")
        self.assertEqual(result, 4)

    def test_single_zero(self):
        result = self.solution.numDecodings("0")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()