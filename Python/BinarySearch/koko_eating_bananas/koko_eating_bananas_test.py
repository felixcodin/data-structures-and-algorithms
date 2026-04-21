import unittest

from koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 4)

    def test_leetcode_example_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 30)

    def test_leetcode_example_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 23)

    def test_single_pile_exact_hours(self):
        piles = [10]
        h = 10
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 1)

    def test_single_pile_one_hour(self):
        piles = [10]
        h = 1
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 10)

    def test_h_equals_number_of_piles(self):
        piles = [5, 9, 7, 3]
        h = 4
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 9)

    def test_large_h_allows_speed_one(self):
        piles = [2, 8, 4]
        h = 100
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 1)

    def test_all_same_piles(self):
        piles = [8, 8, 8, 8]
        h = 8
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 4)

    def test_boundary_needs_rounding_up(self):
        piles = [9, 9, 9]
        h = 4
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 9)

    def test_mixed_small_values(self):
        piles = [1, 2, 3, 4, 5]
        h = 7
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 3)

    def test_very_large_values(self):
        piles = [1_000_000_000, 1_000_000_000]
        h = 3
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 1_000_000_000)

    def test_large_values_with_more_time(self):
        piles = [1_000_000_000, 1_000_000_000]
        h = 4
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 500_000_000)


if __name__ == "__main__":
    unittest.main()
