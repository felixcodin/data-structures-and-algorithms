import unittest
from alternating_group_2 import Solution

class TestAlternatingGroup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testExampleCase(self):
        colors = [0, 1, 0, 0, 1, 0, 1]
        k = 6
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 2)

    def testSingleColor(self):
        colors = [0, 0, 0, 0, 0]
        k = 3
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 0)

    def testAlternatingColors(self):
        colors = [0, 1, 0, 1, 0, 1]
        k = 4
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 6)

    def testSmallK(self):
        colors = [0, 1, 0, 1, 1, 0, 1]
        k = 2
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 6)

    def testLargeK(self):
        colors = [0, 1, 0, 1, 0, 1]
        k = 7
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 0)

    def  testNoAlternatingGroup(self):
        colors = [0, 0, 1, 1, 0, 0]
        k = 3
        res = self.solution.numberOfAlternatingGroup(colors, k)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()