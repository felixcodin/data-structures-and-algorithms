import unittest
from graph_valid_tree import Solution

class TestGraphValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testValidTreeBasic(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        result = self.solution.validTree(n, edges)
        self.assertTrue(result)

    def testCyclePresent(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testSingleNode(self):
        n = 1
        edges = []
        result = self.solution.validTree(n, edges)
        self.assertTrue(result)

    def testZeroNodes(self):
        n = 0
        edges = []
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testTwoNodesConnected(self):
        n = 2
        edges = [[0, 1]]
        result = self.solution.validTree(n, edges)
        self.assertTrue(result)

    def testTwoNodesDisconnected(self):
        n = 2
        edges = []
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testDisconnectedGraph(self):
        n = 4
        edges = [[0, 1], [2, 3]]
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testTooManyEdges(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testTooFewEdges(self):
        n = 4
        edges = [[0, 1], [1, 2]]
        result = self.solution.validTree(n, edges)
        self.assertFalse(result)

    def testLinearTree(self):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3]]
        result = self.solution.validTree(n, edges)
        self.assertTrue(result)

    def testStarTree(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        result = self.solution.validTree(n, edges)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()