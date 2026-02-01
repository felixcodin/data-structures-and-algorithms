import unittest
from number_of_connected_components_in_an_undirected_graph import Solution

class TestNumberOfConnectedComponentsInAnUndirectedGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testBasicCase(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 2)

    def testSingleComponent(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)

    def testAllDisconnected(self):
        n = 4
        edges = []
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 4)

    def testSingleNode(self):
        n = 1
        edges = []
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)

    def testTwoNodes(self):
        n = 2
        edges = [[0, 1]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)

    def testTwoNodesDisconnected(self):
        n = 2
        edges = []
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 2)

    def testMultipleComponents(self):
        n = 7
        edges = [[0, 1], [1, 2], [3, 4], [5, 6]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 3)

    def testCompleteGraph(self):
        n = 4
        edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)

    def testCycleGraph(self):
        n = 4
        edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)

    def testStarGraph(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        result = self.solution.countComponents(n, edges)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()