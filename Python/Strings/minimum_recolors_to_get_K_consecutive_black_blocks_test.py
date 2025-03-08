import unittest
from minimum_recolors_to_get_K_consecutive_black_blocks import Solution

class TestMinimumRecolors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testExampleCase(self):
        blocks = "WBBWWBBWBW"
        k = 7
        res = self.solution.minimumRecolors(blocks, k)
        self.assertEqual(res, 3)

    def testAllBlack(self):
        blocks = "BBBBBBBB"
        k = 4
        res = self.solution.minimumRecolors(blocks, k)
        self.assertEqual(res, 0)

    def testAllWhite(self):
        blocks = "WWWWW"
        k = 2
        res = self.solution.minimumRecolors(blocks, k)
        self.assertEqual(res, 2)

    def testSingleBlocks(self):
        blocks = "W"
        k = 1
        res = self.solution.minimumRecolors(blocks, k)
        self.assertEqual(res, 1)

    def testLargeBlocks(self):
        blocks = "WBWBWWWWBBWBWWBBWBBWWWBBBBWBWWBWWWBWBWWBWBBBBBWBBBBBBBWWB"
        k = 10
        res = self.solution.minimumRecolors(blocks, k)
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()