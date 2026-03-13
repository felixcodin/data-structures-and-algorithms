import unittest
from asteroid_collision import Solution

class TestAsteroidCollision(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # ── Edge / minimal inputs ──────────────────────────────────────────────

    def test_empty_input(self):
        self.assertEqual(self.solution.asteroidCollision([]), [])

    def test_single_positive(self):
        self.assertEqual(self.solution.asteroidCollision([5]), [5])

    def test_single_negative(self):
        self.assertEqual(self.solution.asteroidCollision([-7]), [-7])

    # ── No-collision scenarios ─────────────────────────────────────────────

    def test_all_positive_no_collision(self):
        self.assertEqual(self.solution.asteroidCollision([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_negative_no_collision(self):
        self.assertEqual(self.solution.asteroidCollision([-1, -2, -3, -4]), [-1, -2, -3, -4])

    def test_negatives_before_positives_no_collision(self):
        self.assertEqual(self.solution.asteroidCollision([-3, -2, 1, 4]), [-3, -2, 1, 4])

    # ── Basic single collision ─────────────────────────────────────────────

    def test_negative_smaller_destroyed(self):
        # -5 hits 10: -5 is destroyed
        self.assertEqual(self.solution.asteroidCollision([10, -5]), [10])

    def test_equal_size_mutual_destruction(self):
        # 8 and -8 destroy each other
        self.assertEqual(self.solution.asteroidCollision([8, -8]), [])

    def test_positive_destroyed_by_larger_negative(self):
        # 5 is destroyed by -10
        self.assertEqual(self.solution.asteroidCollision([5, -10]), [-10])

    # ── Chain collisions ───────────────────────────────────────────────────

    def test_negative_destroys_multiple_positives(self):
        # -10 wipes out 1, 2, 3 one by one
        self.assertEqual(self.solution.asteroidCollision([1, 2, 3, -10]), [-10])

    def test_negative_pops_several_then_dies_on_equal(self):
        # -5 destroys 2 and 3, then ties with 5 → both gone
        self.assertEqual(self.solution.asteroidCollision([5, 2, 3, -5]), [])

    def test_negative_pops_several_then_dies_on_larger(self):
        # -4 destroys 2 and 3 but is stopped by 6
        self.assertEqual(self.solution.asteroidCollision([6, 2, 3, -4]), [6])

    def test_large_negative_destroys_all_survivors(self):
        self.assertEqual(self.solution.asteroidCollision([4, 3, 2, -10]), [-10])

    # ── Multiple incoming negatives ────────────────────────────────────────

    def test_two_negatives_destroy_two_positives(self):
        self.assertEqual(self.solution.asteroidCollision([3, 5, -5, -3]), [])

    def test_two_negatives_one_positive_survives(self):
        # -5 kills 3, -5 kills 5, 10 survives
        self.assertEqual(self.solution.asteroidCollision([10, 3, -5, -5]), [10])

    def test_positive_survives_all_smaller_negatives(self):
        self.assertEqual(self.solution.asteroidCollision([10, -1, -2, -3]), [10])

    # ── Mixed surviving asteroids ──────────────────────────────────────────

    def test_survivors_on_both_sides(self):
        # -2 kills 1, -3 kills 2; -2 and -3 remain alongside 4
        self.assertEqual(self.solution.asteroidCollision([1, 2, -2, -3, 4]), [-3, 4])

    def test_negatives_pass_through_empty_stack(self):
        # stack is empty when -5 arrives → it just appends
        self.assertEqual(self.solution.asteroidCollision([-5, -3, 2, 4]), [-5, -3, 2, 4])

    def test_order_of_survivors_preserved(self):
        self.assertEqual(self.solution.asteroidCollision([-6, -4, 3, 8]), [-6, -4, 3, 8])

    # ── LeetCode canonical examples ────────────────────────────────────────

    def test_leetcode_example_5_10_minus5(self):
        self.assertEqual(self.solution.asteroidCollision([5, 10, -5]), [5, 10])

    def test_leetcode_example_10_2_minus5(self):
        self.assertEqual(self.solution.asteroidCollision([10, 2, -5]), [10])

    def test_leetcode_example_minus2_minus1_1_2(self):
        self.assertEqual(self.solution.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])

    # ── Large / stress patterns ────────────────────────────────────────────

    def test_all_same_positive(self):
        self.assertEqual(self.solution.asteroidCollision([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_all_same_negative(self):
        self.assertEqual(self.solution.asteroidCollision([-3, -3, -3, -3]), [-3, -3, -3, -3])

    def test_alternating_equal_all_destroyed(self):
        # each positive is immediately cancelled by the following negative
        self.assertEqual(self.solution.asteroidCollision([1, -1, 2, -2, 3, -3]), [])

    def test_long_chain_single_survivor(self):
        # 100 destroys every positive before it
        self.assertEqual(self.solution.asteroidCollision([1, 2, 3, 4, 5, -100]), [-100])

    def test_large_positive_outlasts_many_negatives(self):
        self.assertEqual(self.solution.asteroidCollision([100, -1, -2, -3, -4, -5]), [100])


if __name__ == "__main__":
    unittest.main()