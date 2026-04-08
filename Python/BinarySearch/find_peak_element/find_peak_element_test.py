import unittest

from find_peak_element import Solution


class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_is_peak(self, nums, idx):
        self.assertTrue(0 <= idx < len(nums), "Returned index out of range")
        left_ok = idx == 0 or nums[idx] > nums[idx - 1]
        right_ok = idx == len(nums) - 1 or nums[idx] > nums[idx + 1]
        self.assertTrue(left_ok and right_ok, f"Index {idx} is not a peak for {nums}")

    def test_single_element(self):
        nums = [10]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 0)

    def test_two_elements_increasing(self):
        nums = [1, 2]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 1)

    def test_two_elements_decreasing(self):
        nums = [2, 1]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 0)

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 4)

    def test_strictly_decreasing(self):
        nums = [9, 7, 5, 3, 1]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 0)

    def test_classic_leetcode_case(self):
        nums = [1, 2, 3, 1]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 2)

    def test_multiple_valid_peaks_case(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        idx = self.solution.findPeakElement(nums)
        self.assertIn(idx, [1, 5])
        self.assert_is_peak(nums, idx)

    def test_peak_in_middle(self):
        nums = [1, 3, 20, 4, 1, 0]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 2)

    def test_peak_at_left_boundary(self):
        nums = [7, 3, 2, 1]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 0)

    def test_peak_at_right_boundary(self):
        nums = [1, 2, 3, 9]
        idx = self.solution.findPeakElement(nums)
        self.assertEqual(idx, 3)

    def test_small_valley(self):
        nums = [3, 1, 2]
        idx = self.solution.findPeakElement(nums)
        self.assertIn(idx, [0, 2])
        self.assert_is_peak(nums, idx)

    def test_large_input_peak_validity(self):
        nums = [1, 3, 2, 5, 4, 8, 7, 9, 6, 10, 0]
        idx = self.solution.findPeakElement(nums)
        self.assert_is_peak(nums, idx)


if __name__ == "__main__":
    unittest.main()
