import unittest
from three_sum import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted([sorted(triplet) for triplet in result]), 
                        sorted([sorted(triplet) for triplet in expected]))

    def testAllPositive(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def testAllNegative(self):
        nums = [-1, -2, -3, -4, -5]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def testWithZeros(self):
        nums = [0, 0, 0, 0]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [[0, 0, 0]])

    def testEmptyInput(self):
        nums = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def testTwoElements(self):
        nums = [1, -1]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def testThreeElements(self):
        nums = [-1, 0, 1]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [[-1, 0, 1]])

    def testDuplicates(self):
        nums = [-2, 0, 0, 2, 2]
        result = self.solution.threeSum(nums)
        expected = [[-2, 0, 2]]
        self.assertEqual(sorted([sorted(triplet) for triplet in result]), 
                        sorted([sorted(triplet) for triplet in expected]))

    def testMultipleTriplets(self):
        nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
        result = self.solution.threeSum(nums)
        self.assertGreater(len(result), 0)
        for triplet in result:
            self.assertEqual(sum(triplet), 0)

    def testNoDuplicateTriplets(self):
        nums = [0, 0, 0, 0, 0]
        result = self.solution.threeSum(nums)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, [[0, 0, 0]])

    def testMixedValues(self):
        nums = [-1, 0, 1, 0]
        result = self.solution.threeSum(nums)
        expected = [[-1, 0, 1]]
        self.assertEqual(sorted([sorted(triplet) for triplet in result]), 
                        sorted([sorted(triplet) for triplet in expected]))


if __name__ == '__main__':
    unittest.main()