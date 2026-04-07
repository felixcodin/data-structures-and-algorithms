import unittest

from successful_pairs_of_spells_and_potions import Solution


class TestSuccessfulPairsOfSpellsAndPotions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [4, 0, 3])

    def test_leetcode_example_2(self):
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [2, 0, 2])

    def test_single_pair_success(self):
        spells = [10]
        potions = [10]
        success = 100
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [1])

    def test_single_pair_not_successful(self):
        spells = [9]
        potions = [10]
        success = 100
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [0])

    def test_all_spells_fail(self):
        spells = [1, 2, 3]
        potions = [1, 1, 1, 1]
        success = 100
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [0, 0, 0])

    def test_all_pairs_success(self):
        spells = [1, 2, 3]
        potions = [5, 6, 7]
        success = 1
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [3, 3, 3])

    def test_duplicate_values(self):
        spells = [4, 4, 4]
        potions = [2, 2, 2, 2]
        success = 8
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [4, 4, 4])

    def test_threshold_boundary(self):
        spells = [2, 3, 4]
        potions = [2, 3, 4]
        success = 8
        # 2 -> [4] => 1, 3 -> [3,4] => 2, 4 -> [2,3,4] => 3
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [1, 2, 3])

    def test_unsorted_potions_input(self):
        spells = [5, 10]
        potions = [4, 1, 10, 3]
        success = 20
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [2, 3])

    def test_large_numbers(self):
        spells = [100000, 99999]
        potions = [100000, 1, 50000]
        success = 10_000_000_000
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [1, 0])

    def test_spells_order_preserved_in_output(self):
        spells = [8, 1, 6]
        potions = [1, 2, 3, 9]
        success = 18
        # 8 -> 2 pairs, 1 -> 0 pairs, 6 -> 2 pair
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [2, 0, 2])

    def test_empty_spells_returns_empty(self):
        spells = []
        potions = [1, 2, 3]
        success = 5
        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [])


if __name__ == "__main__":
    unittest.main()
