import unittest
from coin_change import Solution

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        coins = [1, 2, 5]
        amount = 11
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 3)  # 5 + 5 + 1

    def testAmountZero(self):
        coins = [1, 2, 5]
        amount = 0
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 0)

    def testImpossibleCase(self):
        coins = [2]
        amount = 3
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, -1)

    def testSingleCoin(self):
        coins = [1]
        amount = 5
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 5)

    def testExactMatch(self):
        coins = [5]
        amount = 5
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 1)

    def testMultipleCoins(self):
        coins = [1, 3, 4]
        amount = 6
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2)  # 3 + 3

    def testLargeAmount(self):
        coins = [1, 5, 10, 25]
        amount = 63
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 6)  # 25 + 25 + 10 + 1 + 1 + 1

    def testCoinsLargerThanAmount(self):
        coins = [5, 10]
        amount = 3
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, -1)

    def testAmountOne(self):
        coins = [1]
        amount = 1
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 1)

    def testLargeCoins(self):
        coins = [2, 5, 10, 1]
        amount = 27
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 4)  # 10 + 10 + 5 + 2

    def testGreedyWouldFail(self):
        coins = [1, 3, 4]
        amount = 6
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2)  # 3 + 3, not 4 + 1 + 1

    def testOnlyLargeCoins(self):
        coins = [5, 10]
        amount = 15
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2)  # 10 + 5 or 5 + 5 + 5


if __name__ == '__main__':
    unittest.main()