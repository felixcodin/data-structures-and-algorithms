import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def testRandomElements(self):
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 2])

    def testDuplicatesElements(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def testAscendingArray(self):
        nums = [1, 2, 3, 4, 5]
        target = 8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [2, 4])

    def testArrayWithZero(self):
        nums = [0, 4, 3, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 3])

if __name__ == '__main__':
    unittest.main()