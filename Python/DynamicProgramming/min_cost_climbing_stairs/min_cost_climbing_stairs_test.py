import unittest
from min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLeetCodeExample1(self):
        # Start from index 1, pay 15, reach the top
        result = self.solution.minCostClimbingStairs([10, 15, 20])
        self.assertEqual(result, 15)

    def testLeetCodeExample2(self):
        # Optimal path: start at index 1, step on indices 1, 2, 4, 6, 7, 9
        result = self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        self.assertEqual(result, 6)

    def testMinimumLength(self):
        # With only 2 elements, choose the smaller one
        result = self.solution.minCostClimbingStairs([10, 15])
        self.assertEqual(result, 10)

    def testEqualCosts(self):
        # All steps have equal cost
        result = self.solution.minCostClimbingStairs([5, 5, 5, 5])
        self.assertEqual(result, 10)

    def testIncreasingCosts(self):
        # Costs increase progressively
        result = self.solution.minCostClimbingStairs([1, 2, 3, 4, 5])
        self.assertEqual(result, 6)

    def testDecreasingCosts(self):
        # Costs decrease progressively
        result = self.solution.minCostClimbingStairs([5, 4, 3, 2, 1])
        self.assertEqual(result, 6)

    def testAlternatingHighLow(self):
        # Alternating between low and high costs
        result = self.solution.minCostClimbingStairs([1, 100, 1, 100, 1])
        self.assertEqual(result, 3)

    def testStartFromFirstBetter(self):
        # Starting from index 0 is better
        result = self.solution.minCostClimbingStairs([0, 1, 2, 2])
        self.assertEqual(result, 2)

    def testStartFromSecondBetter(self):
        # Starting from index 1 is better
        result = self.solution.minCostClimbingStairs([1, 0, 2, 2])
        self.assertEqual(result, 2)

    def testLargerArray(self):
        # Larger array with mixed costs
        result = self.solution.minCostClimbingStairs([10, 15, 20, 5, 2, 3, 10, 8])
        self.assertEqual(result, 31)

    def testAllZeros(self):
        # All steps are free
        result = self.solution.minCostClimbingStairs([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def testSingleHighCostAtEnd(self):
        # High cost at the end shouldn't affect optimal path
        result = self.solution.minCostClimbingStairs([1, 1, 1, 1, 100])
        self.assertEqual(result, 2)

    def testHighCostsAtStart(self):
        # High costs at the start, low costs later
        result = self.solution.minCostClimbingStairs([100, 100, 1, 1, 1])
        self.assertEqual(result, 101)

    def testTwoElementsFirstCheaper(self):
        # First element is cheaper
        result = self.solution.minCostClimbingStairs([5, 10])
        self.assertEqual(result, 5)

    def testTwoElementsSecondCheaper(self):
        # Second element is cheaper
        result = self.solution.minCostClimbingStairs([10, 5])
        self.assertEqual(result, 5)

    def testThreeElements(self):
        # Three elements test
        result = self.solution.minCostClimbingStairs([1, 2, 3])
        self.assertEqual(result, 2)

    def testFourElements(self):
        # Four elements with varying costs
        result = self.solution.minCostClimbingStairs([5, 10, 15, 20])
        self.assertEqual(result, 20)

    def testLargeNumbers(self):
        # Test with larger cost values
        result = self.solution.minCostClimbingStairs([1000, 1, 1000, 1, 1000])
        self.assertEqual(result, 2)

    def testZeroAndNonZero(self):
        # Mix of zero and non-zero costs
        result = self.solution.minCostClimbingStairs([0, 2, 0, 2, 0])
        self.assertEqual(result, 0)

    def testGradualIncrease(self):
        # Gradual increase in costs
        result = self.solution.minCostClimbingStairs([1, 2, 4, 8, 16])
        self.assertEqual(result, 10)

    def testPeakInMiddle(self):
        # High costs in the middle
        result = self.solution.minCostClimbingStairs([1, 1, 100, 1, 1])
        self.assertEqual(result, 2)

    def testValleyInMiddle(self):
        # Low costs in the middle
        result = self.solution.minCostClimbingStairs([10, 10, 1, 10, 10])
        self.assertEqual(result, 20)

    def testLongArrayUniformCost(self):
        # Long array with uniform cost
        result = self.solution.minCostClimbingStairs([3] * 10)
        self.assertEqual(result, 15)

    def testLongArrayIncreasing(self):
        # Long array with increasing costs
        result = self.solution.minCostClimbingStairs(list(range(1, 11)))
        self.assertEqual(result, 25)

    def testOptimalPathSkipsExpensive(self):
        # Optimal path should skip expensive steps
        result = self.solution.minCostClimbingStairs([1, 100, 2, 3, 100, 1])
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()