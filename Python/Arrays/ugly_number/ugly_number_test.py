import unittest

from ugly_number import Solution


class TestUglyNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_is_ugly(self) -> None:
        self.assertTrue(self.solution.isUgly(1))

    def test_example_true(self) -> None:
        self.assertTrue(self.solution.isUgly(6))

    def test_example_false(self) -> None:
        self.assertFalse(self.solution.isUgly(14))

    def test_zero_is_not_ugly(self) -> None:
        self.assertFalse(self.solution.isUgly(0))

    def test_negative_number_is_not_ugly(self) -> None:
        self.assertFalse(self.solution.isUgly(-6))

    def test_powers_of_allowed_primes(self) -> None:
        cases = [2, 3, 5, 8, 9, 25, 27, 125]
        for value in cases:
            with self.subTest(value=value):
                self.assertTrue(self.solution.isUgly(value))

    def test_numbers_with_other_prime_factors(self) -> None:
        cases = [7, 11, 13, 21, 22, 26, 77]
        for value in cases:
            with self.subTest(value=value):
                self.assertFalse(self.solution.isUgly(value))


if __name__ == "__main__":
    unittest.main()
