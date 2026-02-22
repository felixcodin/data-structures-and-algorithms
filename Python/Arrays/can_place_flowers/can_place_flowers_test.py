import unittest
from can_place_flowers import Solution


class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCanPlace(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testBasicCannotPlace(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testLeetCodeExample1(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testLeetCodeExample2(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testZeroFlowers(self):
        flowerbed = [1, 0, 1, 0, 1]
        n = 0
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testSinglePlotEmpty(self):
        flowerbed = [0]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testSinglePlotEmptyCannotPlace(self):
        flowerbed = [0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testSinglePlotOccupied(self):
        flowerbed = [1]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testSinglePlotOccupiedZeroNeeded(self):
        flowerbed = [1]
        n = 0
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testAllEmpty(self):
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testAllEmptyCannotPlace(self):
        flowerbed = [0, 0, 0, 0, 0]
        n = 4
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testAllOccupied(self):
        flowerbed = [1, 0, 1, 0, 1]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testTwoPlots(self):
        flowerbed = [0, 0]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testTwoPlotsCannotPlace(self):
        flowerbed = [0, 0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testTwoPlotsWithOne(self):
        flowerbed = [1, 0]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testThreePlotsEmpty(self):
        flowerbed = [0, 0, 0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testStartWithEmpty(self):
        flowerbed = [0, 0, 1, 0, 0]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testEndWithEmpty(self):
        flowerbed = [1, 0, 0, 0, 0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testConsecutiveEmpty(self):
        flowerbed = [0, 0, 0, 0, 0, 0, 0]
        n = 4
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testConsecutiveEmptyCannotPlace(self):
        flowerbed = [0, 0, 0, 0, 0, 0, 0]
        n = 5
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testAlternatingPattern(self):
        flowerbed = [1, 0, 1, 0, 1, 0, 1]
        n = 1
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testMultipleGaps(self):
        flowerbed = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testMultipleGapsCannotPlace(self):
        flowerbed = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        n = 3
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testLongEmptyStart(self):
        flowerbed = [0, 0, 0, 0, 1]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testLongEmptyEnd(self):
        flowerbed = [1, 0, 0, 0, 0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testExactlyEnoughSpace(self):
        flowerbed = [0, 0, 0, 0, 0, 0]
        n = 3
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testLargeFlowerbed(self):
        flowerbed = [0] * 20
        n = 10
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testLargeFlowerbedCannotPlace(self):
        flowerbed = [0] * 20
        n = 11
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertFalse(result)

    def testComplexPattern(self):
        flowerbed = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testFourEmpty(self):
        flowerbed = [0, 0, 0, 0]
        n = 2
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)

    def testFiveEmpty(self):
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        result = self.solution.canPlaceFlowers(flowerbed, n)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()