import unittest

from water_and_jug_problem import Solution


class TestWaterAndJugProblem(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_true(self):
        self.assertTrue(self.solution.canMeasureWater(3, 5, 4))

    def test_target_greater_than_total_capacity(self):
        self.assertFalse(self.solution.canMeasureWater(2, 6, 10))

    def test_target_equal_total_capacity(self):
        self.assertTrue(self.solution.canMeasureWater(2, 6, 8))

    def test_target_zero_with_nonzero_jugs(self):
        self.assertTrue(self.solution.canMeasureWater(3, 5, 0))

    def test_gcd_divides_target_true(self):
        self.assertTrue(self.solution.canMeasureWater(6, 10, 8))

    def test_gcd_does_not_divide_target_false(self):
        self.assertFalse(self.solution.canMeasureWater(6, 10, 7))

    def test_same_size_jugs_measure_possible(self):
        self.assertTrue(self.solution.canMeasureWater(4, 4, 4))

    def test_same_size_jugs_measure_impossible(self):
        self.assertFalse(self.solution.canMeasureWater(4, 4, 2))

    def test_one_jug_zero_target_possible(self):
        self.assertTrue(self.solution.canMeasureWater(0, 5, 5))

    def test_one_jug_zero_target_impossible(self):
        self.assertFalse(self.solution.canMeasureWater(0, 5, 3))

    def test_large_values_true_case(self):
        self.assertTrue(self.solution.canMeasureWater(104, 168, 8))

    def test_large_values_false_case(self):
        self.assertFalse(self.solution.canMeasureWater(104, 168, 7))


if __name__ == "__main__":
    unittest.main()
