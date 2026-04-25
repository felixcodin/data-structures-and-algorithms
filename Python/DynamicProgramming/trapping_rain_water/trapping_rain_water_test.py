import unittest

from trapping_rain_water import Solution


class TestTrappingRainWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.solution.trap(height), 6)

    def test_leetcode_example_2(self):
        height = [4, 2, 0, 3, 2, 5]
        self.assertEqual(self.solution.trap(height), 9)

    def test_strictly_increasing(self):
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.trap(height), 0)

    def test_strictly_decreasing(self):
        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.trap(height), 0)

    def test_all_equal_heights(self):
        height = [3, 3, 3, 3]
        self.assertEqual(self.solution.trap(height), 0)

    def test_single_bar(self):
        height = [7]
        self.assertEqual(self.solution.trap(height), 0)

    def test_two_bars(self):
        height = [2, 5]
        self.assertEqual(self.solution.trap(height), 0)

    def test_simple_valley(self):
        height = [2, 0, 2]
        self.assertEqual(self.solution.trap(height), 2)

    def test_multiple_valleys(self):
        height = [3, 0, 1, 3, 0, 5]
        self.assertEqual(self.solution.trap(height), 8)

    def test_all_zero_heights(self):
        height = [0, 0, 0, 0]
        self.assertEqual(self.solution.trap(height), 0)

    def test_large_boundary_walls(self):
        height = [5, 0, 0, 0, 5]
        self.assertEqual(self.solution.trap(height), 15)

    def test_small_mixed_case(self):
        height = [5, 4, 1, 2]
        self.assertEqual(self.solution.trap(height), 1)

    def test_empty_list_current_behavior(self):
        with self.assertRaises(IndexError):
            self.solution.trap([])


if __name__ == "__main__":
    unittest.main()
