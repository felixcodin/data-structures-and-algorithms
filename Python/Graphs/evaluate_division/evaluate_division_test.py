import unittest
from evaluate_division import Solution


class TestEvaluateDivision(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertResultListAlmostEqual(self, actual, expected, places=9):
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            if e == -1:
                self.assertEqual(a, -1)
            else:
                self.assertAlmostEqual(a, e, places=places)

    def test_leetcode_sample_case(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1, 1.0, -1]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_direct_and_reverse_queries(self):
        equations = [["usd", "eur"]]
        values = [0.8]
        queries = [["usd", "eur"], ["eur", "usd"]]
        expected = [0.8, 1.25]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_multi_hop_chain_forward_and_reverse(self):
        equations = [["a", "b"], ["b", "c"], ["c", "d"]]
        values = [2.0, 3.0, 4.0]
        queries = [["a", "d"], ["d", "a"], ["b", "d"], ["d", "b"]]
        expected = [24.0, 1 / 24.0, 12.0, 1 / 12.0]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_disconnected_components(self):
        equations = [["a", "b"], ["c", "d"]]
        values = [2.0, 5.0]
        queries = [["a", "b"], ["b", "a"], ["c", "d"], ["a", "d"], ["b", "c"]]
        expected = [2.0, 0.5, 5.0, -1, -1]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_existing_variable_self_query(self):
        equations = [["x", "y"], ["y", "z"]]
        values = [4.0, 0.5]
        queries = [["x", "x"], ["y", "y"], ["z", "z"]]
        expected = [1.0, 1.0, 1.0]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_empty_equations_all_unknown(self):
        equations = []
        values = []
        queries = [["a", "b"], ["a", "a"], ["x", "x"]]
        expected = [-1, -1, -1]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_decimal_values_precision(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [1.5, 2.5]
        queries = [["a", "c"], ["c", "a"], ["c", "b"], ["b", "a"]]
        expected = [3.75, 1 / 3.75, 1 / 2.5, 1 / 1.5]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_longer_chain_product(self):
        equations = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
        values = [2.0, 2.0, 2.0, 2.0]
        queries = [["a", "e"], ["e", "a"], ["b", "e"], ["a", "d"]]
        expected = [16.0, 1 / 16.0, 8.0, 8.0]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_partial_unknown_variables(self):
        equations = [["m", "n"], ["n", "o"]]
        values = [3.0, 7.0]
        queries = [["m", "p"], ["p", "m"], ["p", "p"], ["o", "m"]]
        expected = [-1, -1, -1, 1 / 21.0]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)

    def test_component_with_branch_queries(self):
        equations = [["a", "b"], ["a", "c"], ["c", "d"]]
        values = [2.0, 3.0, 4.0]
        queries = [["b", "d"], ["d", "b"], ["b", "c"], ["c", "b"]]
        # b->a->c->d = (1/2)*3*4 = 6
        expected = [6.0, 1 / 6.0, 1.5, 2 / 3.0]
        actual = self.solution.calcEquation(equations, values, queries)
        self.assertResultListAlmostEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()