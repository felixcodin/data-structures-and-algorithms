import unittest
from dota2_senate import Solution


class TestDota2Senate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        senate = "RD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testLeetCodeExample1(self):
        senate = "RD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testLeetCodeExample2(self):
        senate = "RDD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testSingleRadiant(self):
        senate = "R"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testSingleDire(self):
        senate = "D"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testAllRadiant(self):
        senate = "RRRR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testAllDire(self):
        senate = "DDDD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testTwoSenatorsDireFirst(self):
        senate = "DR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testTwoRadiantOneDire(self):
        senate = "RRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testTwoDireOneRadiant(self):
        senate = "DDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testAlternatingStartingWithRadiant(self):
        senate = "RDRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testAlternatingStartingWithDire(self):
        senate = "DRDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testOddLengthAlternatingRadiantWins(self):
        senate = "RDRDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testOddLengthAlternatingDireWins(self):
        senate = "DRDRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testGroupedRadiantWins(self):
        senate = "RRRDD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testGroupedDireWins(self):
        senate = "DDDRR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testDireMinorityWinsBecauseOfOrder(self):
        senate = "DDRRR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testRadiantMinorityWinsBecauseOfOrder(self):
        senate = "RRDDD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testMixedPatternRadiantWins(self):
        senate = "RDDRRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testMixedPatternDireWins(self):
        senate = "DDRRRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testLongerPatternRadiantWins(self):
        senate = "RRDDDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testLongerPatternDireWins(self):
        senate = "RDDD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testClusterThenAlternationRadiantWins(self):
        senate = "RRDRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testClusterThenAlternationDireWins(self):
        senate = "DDRDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")

    def testManyRadiantAgainstOneDire(self):
        senate = "RRRRD"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Radiant")

    def testManyDireAgainstOneRadiant(self):
        senate = "DDDDR"
        result = self.solution.predictPartyVictory(senate)
        self.assertEqual(result, "Dire")


if __name__ == "__main__":
    unittest.main()