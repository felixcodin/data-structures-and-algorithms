import unittest

import guess_number_higher_or_lower as module
from guess_number_higher_or_lower import Solution, guess, set_picked_number


class TestGuessNumberHigherOrLower(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_api_returns_zero_when_equal(self):
        set_picked_number(5)
        self.assertEqual(guess(5), 0)

    def test_api_returns_one_when_guess_is_lower(self):
        set_picked_number(5)
        self.assertEqual(guess(3), 1)

    def test_api_returns_minus_one_when_guess_is_higher(self):
        set_picked_number(5)
        self.assertEqual(guess(7), -1)

    def test_api_raises_if_not_initialized(self):
        # Reset internal state for this test.
        module._picked_number = None
        with self.assertRaises(ValueError):
            guess(1)

    def test_guess_number_n_1(self):
        set_picked_number(1)
        self.assertEqual(self.solution.guessNumber(1), 1)

    def test_guess_number_left_boundary(self):
        set_picked_number(1)
        self.assertEqual(self.solution.guessNumber(10), 1)

    def test_guess_number_right_boundary(self):
        set_picked_number(10)
        self.assertEqual(self.solution.guessNumber(10), 10)

    def test_guess_number_middle_value(self):
        set_picked_number(6)
        self.assertEqual(self.solution.guessNumber(10), 6)

    def test_guess_number_even_range(self):
        set_picked_number(14)
        self.assertEqual(self.solution.guessNumber(20), 14)

    def test_guess_number_large_range(self):
        set_picked_number(1702766719)
        self.assertEqual(self.solution.guessNumber(2126753390), 1702766719)

    def test_guess_number_random_case_1(self):
        set_picked_number(73)
        self.assertEqual(self.solution.guessNumber(100), 73)

    def test_guess_number_random_case_2(self):
        set_picked_number(999)
        self.assertEqual(self.solution.guessNumber(1000), 999)


if __name__ == "__main__":
    unittest.main()
