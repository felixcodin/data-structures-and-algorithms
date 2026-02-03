import unittest
from climbing_stairs import Solution

class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testOneStep(self):
        n = 1
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 1)

    def testTwoSteps(self):
        n = 2
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 2)

    def testThreeSteps(self):
        n = 3
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 3)

    def testFourSteps(self):
        n = 4
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 5)

    def testFiveSteps(self):
        n = 5
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 8)

    def testTenSteps(self):
        n = 10
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 89)

    def testFifteenSteps(self):
        n = 15
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 987)

    def testTwentySteps(self):
        n = 20
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 10946)


if __name__ == '__main__':
    unittest.main()