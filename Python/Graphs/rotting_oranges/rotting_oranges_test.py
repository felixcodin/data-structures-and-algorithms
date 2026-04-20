import unittest
from rotting_oranges import Solution


class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertRottingTime(self, grid, expected):
        grid_copy = [row[:] for row in grid]
        self.assertEqual(self.solution.orangesRotting(grid_copy), expected)

    def test_leetcode_example_reachable(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]
        self.assertRottingTime(grid, 4)

    def test_leetcode_example_unreachable(self):
        grid = [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1],
        ]
        self.assertRottingTime(grid, -1)

    def test_no_fresh_oranges_returns_zero(self):
        grid = [
            [0, 2],
            [2, 0],
        ]
        self.assertRottingTime(grid, 0)

    def test_single_fresh_no_rotten_source(self):
        grid = [[1]]
        self.assertRottingTime(grid, -1)

    def test_single_rotten_orange(self):
        grid = [[2]]
        self.assertRottingTime(grid, 0)

    def test_all_empty_cells(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertRottingTime(grid, 0)

    def test_one_minute_to_rot(self):
        grid = [[2, 1]]
        self.assertRottingTime(grid, 1)

    def test_linear_chain_spread(self):
        grid = [[2, 1, 1, 1]]
        self.assertRottingTime(grid, 3)

    def test_multiple_initial_rotten_sources(self):
        grid = [
            [2, 1, 1],
            [1, 1, 1],
            [1, 1, 2],
        ]
        self.assertRottingTime(grid, 2)

    def test_isolated_fresh_due_to_zeros(self):
        grid = [[2, 0, 1]]
        self.assertRottingTime(grid, -1)

    def test_reachable_with_empty_spaces(self):
        grid = [
            [2, 1, 0, 1],
            [1, 1, 1, 1],
            [0, 1, 0, 1],
        ]
        self.assertRottingTime(grid, 5)

    def test_empty_grid_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.solution.orangesRotting([])


if __name__ == "__main__":
    unittest.main()