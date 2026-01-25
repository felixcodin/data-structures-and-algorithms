import unittest
from combination_sum import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        result = self.solution.combinationSum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        self.assertEqual(sorted(result), sorted(expected))

    def testMultipleCombinations(self):
        result = self.solution.combinationSum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(sorted(result), sorted(expected))

    def testSingleElement(self):
        result = self.solution.combinationSum([2], 1)
        self.assertEqual(result, [])

    def testSingleElementMatch(self):
        result = self.solution.combinationSum([1], 1)
        expected = [[1]]
        self.assertEqual(result, expected)

    def testSingleElementMultipleUse(self):
        result = self.solution.combinationSum([1], 3)
        expected = [[1, 1, 1]]
        self.assertEqual(result, expected)

    def testNoSolution(self):
        result = self.solution.combinationSum([2, 4, 6], 5)
        self.assertEqual(result, [])

    def testTargetZero(self):
        result = self.solution.combinationSum([1, 2, 3], 0)
        self.assertEqual(result, [])

    def testLargerNumbers(self):
        result = self.solution.combinationSum([8, 7, 4, 3], 11)
        expected = [[3, 4, 4], [3, 8], [4, 7]]
        self.assertEqual(sorted(result), sorted(expected))

    def testAllSameNumber(self):
        result = self.solution.combinationSum([5, 5, 5], 10)
        expected = [[5, 5]]
        self.assertEqual(result, expected)

    def testRepeatedUseOfSameNumber(self):
        result = self.solution.combinationSum([2], 8)
        expected = [[2, 2, 2, 2]]
        self.assertEqual(result, expected)

    def testMultipleWaysToTarget(self):
        result = self.solution.combinationSum([1, 2, 3], 4)
        expected = [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
        self.assertEqual(sorted(result), sorted(expected))

    def testLargeTarget(self):
        result = self.solution.combinationSum([2, 3, 6], 12)
        expected = [[2, 2, 2, 2, 2, 2], [2, 2, 2, 3, 3], [2, 2, 2, 6], [3, 3, 3, 3], [3, 3, 6], [6, 6]]
        # Check length matches as ordering might differ
        self.assertEqual(len(result), len(expected))

    def testUnsortedInput(self):
        result = self.solution.combinationSum([7, 3, 2], 7)
        expected = [[2, 2, 3], [7]]
        self.assertEqual(sorted(result), sorted(expected))

    def testOneElementExceedsTarget(self):
        result = self.solution.combinationSum([10, 1, 2], 3)
        expected = [[1, 1, 1], [1, 2]]
        self.assertEqual(sorted(result), sorted(expected))

    def testExactMatch(self):
        result = self.solution.combinationSum([5], 5)
        expected = [[5]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()