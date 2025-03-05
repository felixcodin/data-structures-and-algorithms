import unittest
from combination_sum_II import Solution

class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_example_case(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    def test_single_element(self):
        candidates = [5]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[5]])
    def test_no_possible(self):
        candidates = [3]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [])
    def test_multiple_element(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[1, 2, 2], [5]])        
    def test_all_elements_are_the_same(self):
        candidates = [1, 1, 1, 1, 1]
        target = 3
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[1, 1, 1]])
    def test_large_target_with_multiple_combinations(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 15
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[1, 1, 2, 5, 6], [1, 1, 6, 7], [1, 2, 5, 7], [2, 6, 7], [5, 10]])
    def test_empty_candidates_array(self):
        candidates = []
        target = 3
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [])
    def test_target_is_zero(self):
        candidates = [1, 2, 3]
        target = 0
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[]])
    def test_large_numbers_in_candidates(self):
        candidates = [10, 20, 30, 40]
        target = 30
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, [[10, 20], [30]])

if __name__ == '__main__':
    unittest.main()