import unittest
from functools import lru_cache

from guess_number_higher_or_lower_ii import Solution


class TestGuessNumberHigherOrLowerII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    @staticmethod
    def brute_force(n: int) -> int:
        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right:
                return 0
            best = float("inf")
            for guess in range(left, right + 1):
                cost = guess + max(solve(left, guess - 1), solve(guess + 1, right))
                best = min(best, cost)
            return best

        return solve(1, n)

    def test_base_case(self) -> None:
        self.assertEqual(self.solution.getMoneyAmount(1), 0)

    def test_known_values(self) -> None:
        expected = {
            2: 1,
            3: 2,
            4: 4,
            5: 6,
            6: 8,
            7: 10,
            8: 12,
            9: 14,
            10: 16,
        }
        for n, answer in expected.items():
            with self.subTest(n=n):
                self.assertEqual(self.solution.getMoneyAmount(n), answer)

    def test_matches_bruteforce_for_small_n(self) -> None:
        for n in range(1, 9):
            with self.subTest(n=n):
                self.assertEqual(self.solution.getMoneyAmount(n), self.brute_force(n))


if __name__ == "__main__":
    unittest.main()
