import unittest

from find_indices_with_index_and_value_difference_i import Solution


class TestFindIndicesWithIndexAndValueDifferenceI(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    @staticmethod
    def has_valid_pair(nums, index_difference, value_difference):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= index_difference and abs(nums[i] - nums[j]) >= value_difference:
                    return True
        return False

    def assertResultValid(self, nums, index_difference, value_difference, result):
        if result == [-1, -1]:
            self.assertFalse(self.has_valid_pair(nums, index_difference, value_difference))
            return

        self.assertEqual(len(result), 2)
        i, j = result
        self.assertGreaterEqual(i, 0)
        self.assertGreaterEqual(j, 0)
        self.assertLess(i, len(nums))
        self.assertLess(j, len(nums))
        self.assertGreaterEqual(abs(i - j), index_difference)
        self.assertGreaterEqual(abs(nums[i] - nums[j]), value_difference)

    def test_example_with_solution(self):
        nums = [5, 1, 4, 1]
        result = self.solution.findIndices(nums, 2, 4)
        self.assertEqual(result, [0, 3])

    def test_example_no_solution(self):
        nums = [1, 2, 3]
        result = self.solution.findIndices(nums, 2, 4)
        self.assertEqual(result, [-1, -1])

    def test_zero_value_difference(self):
        nums = [1, 2, 3, 4]
        result = self.solution.findIndices(nums, 2, 0)
        self.assertResultValid(nums, 2, 0, result)

    def test_negative_numbers(self):
        nums = [-10, -3, -7, -1]
        result = self.solution.findIndices(nums, 1, 6)
        self.assertResultValid(nums, 1, 6, result)

    def test_exact_index_gap(self):
        nums = [9, 1, 8, 2, 7]
        result = self.solution.findIndices(nums, 3, 6)
        self.assertResultValid(nums, 3, 6, result)

    def test_single_possible_pair(self):
        nums = [1, 10]
        result = self.solution.findIndices(nums, 1, 9)
        self.assertEqual(result, [0, 1])

    def test_no_pair_due_to_index_difference(self):
        nums = [1, 100, 1]
        result = self.solution.findIndices(nums, 3, 50)
        self.assertEqual(result, [-1, -1])

    def test_random_shape_array(self):
        nums = [4, 2, 7, 1, 9, 3]
        result = self.solution.findIndices(nums, 2, 5)
        self.assertResultValid(nums, 2, 5, result)


if __name__ == "__main__":
    unittest.main()
