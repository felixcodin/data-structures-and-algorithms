import unittest

from concatenation_of_array import Solution


class TestConcatenationOfArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self) -> None:
        nums = [1, 2, 1]
        self.assertEqual(self.solution.getConcatenation(nums), [1, 2, 1, 1, 2, 1])

    def test_example_2(self) -> None:
        nums = [1, 3, 2, 1]
        self.assertEqual(self.solution.getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])

    def test_empty_list(self) -> None:
        nums = []
        self.assertEqual(self.solution.getConcatenation(nums), [])

    def test_single_element(self) -> None:
        nums = [7]
        self.assertEqual(self.solution.getConcatenation(nums), [7, 7])

    def test_does_not_change_expected_result_for_duplicates(self) -> None:
        nums = [5, 5, 5]
        self.assertEqual(self.solution.getConcatenation(nums), [5, 5, 5, 5, 5, 5])

    def test_mutates_input_in_place(self) -> None:
        nums = [9, 8]
        result = self.solution.getConcatenation(nums)
        self.assertIs(result, nums)
        self.assertEqual(nums, [9, 8, 9, 8])


if __name__ == "__main__":
    unittest.main()
