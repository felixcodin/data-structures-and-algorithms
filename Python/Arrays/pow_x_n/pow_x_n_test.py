import unittest
from pow_x_n import Solution

class TestMyPow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testPositiveExponent(self):
        res = self.solution.myPow(2, 10)
        self.assertEqual(res, 1024)

    def testNegativeExponent(self):
        res = self.solution.myPow(2, -2)
        self.assertEqual(res, 0.25)

    def testExponentIsZero(self):
        res = self.solution.myPow(2, 0)
        self.assertEqual(res, 1)

    def testBaseIsOne(self):
        res = self.solution.myPow(1, 100)
        self.assertEqual(res, 1)

    def testBaseIsNegativeEvenExponent(self):
        res = self.solution.myPow(-2, 4)
        self.assertEqual(res, 16)
    
    def testBaseIsNegativeOddExponent(self):
        res = self.solution.myPow(-2, 3)
        self.assertEqual(res, -8)

    def testLargeExponent(self):
        res = self.solution.myPow(2, 30)
        self.assertEqual(res, 1073741824)

    def testFractionalBasePositiveExponent(self):
        res = self.solution.myPow(0.5, 3)
        self.assertEqual(res, 0.125)
    
    def testFractionalBaseNegativeExponent(self):
        res = self.solution.myPow(0.5, -2)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()