import unittest
from number_of_senior_citizens import Solution

class TestNumberOfSeniorCitizens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testExampleCase1(self):
        details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 2)

    def testExampleCase2(self):
        details = ["1313579440F2036", "2921522980M5644"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 0)

    def testAllSeniors(self):
        details = ["9876543210M6500", "1234567890F7000", "5555555555M8012"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 3)

    def testNoSeniors(self):
        details = ["1111111111M3012", "2222222222F4523", "3333333333M6011"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 0)

    def testExactly60(self):
        details = ["1234567890M6000"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 0)

    def testExactly61(self):
        details = ["1234567890M6100"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 1)

    def testEmptyList(self):
        details = []
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 0)

    def testSingleSenior(self):
        details = ["9999999999F9999"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 1)

    def testSingleNonSenior(self):
        details = ["1111111111M1811"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 0)

    def testMixedAges(self):
        details = ["1234567890M2512", "2345678901F6523", "3456789012M5034", "4567890123F7045"]
        res = self.solution.countSeniors(details)
        self.assertEqual(res, 2)

if __name__ == '__main__':
    unittest.main()