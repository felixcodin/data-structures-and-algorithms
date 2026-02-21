import unittest
from kids_with_the_greatest_number_of_candies import Solution

class TestKidsWithCandies(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, False, True])

    def testLeetCodeExample1(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, False, True])

    def testLeetCodeExample2(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False, False, False, False])

    def testLeetCodeExample3(self):
        candies = [12, 1, 12]
        extraCandies = 10
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False, True])

    def testSingleKid(self):
        candies = [5]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True])

    def testAllKidsCanReachMax(self):
        candies = [1, 2, 3, 4, 5]
        extraCandies = 10
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, True, True])

    def testNoKidsCanReachMax(self):
        candies = [1, 1, 1, 10]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [False, False, False, True])

    def testZeroExtraCandies(self):
        candies = [5, 3, 8, 2, 8]
        extraCandies = 0
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [False, False, True, False, True])

    def testAllSameCandies(self):
        candies = [5, 5, 5, 5]
        extraCandies = 1
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, True])

    def testAllSameCandiesZeroExtra(self):
        candies = [3, 3, 3]
        extraCandies = 0
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True])

    def testTwoKids(self):
        candies = [10, 5]
        extraCandies = 3
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False])

    def testTwoKidsBothCanReach(self):
        candies = [7, 8]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True])

    def testAscendingOrder(self):
        candies = [1, 2, 3, 4, 5]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [False, False, True, True, True])

    def testDescendingOrder(self):
        candies = [5, 4, 3, 2, 1]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, False, False])

    def testOnlyOneKidHasMax(self):
        candies = [1, 1, 1, 1, 10]
        extraCandies = 5
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [False, False, False, False, True])

    def testExactlyReachMax(self):
        candies = [5, 3, 7, 2]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False, True, False])

    def testLargeExtraCandies(self):
        candies = [1, 2, 3]
        extraCandies = 100
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True])

    def testMultipleMaxValues(self):
        candies = [10, 5, 10, 3, 10]
        extraCandies = 0
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False, True, False, True])

    def testCloseValues(self):
        candies = [9, 10, 9, 10]
        extraCandies = 1
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, True, True, True])

    def testMixedValues(self):
        candies = [8, 2, 5, 7, 3]
        extraCandies = 2
        result = self.solution.kidsWithCandies(candies, extraCandies)
        self.assertEqual(result, [True, False, False, True, False])


if __name__ == '__main__':
    unittest.main()