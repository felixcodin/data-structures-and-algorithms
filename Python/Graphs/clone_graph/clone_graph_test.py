import unittest
from clone_graph import Solution, Node

class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _graphs_equal(self, node1, node2, visited=None):
        """Helper method to check if two graphs are equal"""
        if visited is None:
            visited = set()
        
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        if len(node1.neighbors) != len(node2.neighbors):
            return False
        
        # Check that nodes are actually cloned (different objects)
        if node1 is node2:
            return False
        
        visited.add(node1.val)
        
        neighbor_vals1 = sorted([n.val for n in node1.neighbors])
        neighbor_vals2 = sorted([n.val for n in node2.neighbors])
        
        if neighbor_vals1 != neighbor_vals2:
            return False
        
        # Recursively check neighbors
        for nei1 in node1.neighbors:
            if nei1.val not in visited:
                # Find corresponding neighbor in node2
                nei2 = next((n for n in node2.neighbors if n.val == nei1.val), None)
                if not self._graphs_equal(nei1, nei2, visited):
                    return False
        
        return True

    def testEmptyGraph(self):
        result = self.solution.cloneGraph(None)
        self.assertIsNone(result)

    def testSingleNode(self):
        node = Node(1)
        cloned = self.solution.cloneGraph(node)
        self.assertIsNotNone(cloned)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 0)
        self.assertIsNot(node, cloned)

    def testTwoConnectedNodes(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        self.assertTrue(self._graphs_equal(node1, cloned))

    def testLinearGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.neighbors = [node2]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2]
        
        cloned = self.solution.cloneGraph(node1)
        self.assertTrue(self._graphs_equal(node1, cloned))

    def testSquareGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        
        cloned = self.solution.cloneGraph(node1)
        self.assertTrue(self._graphs_equal(node1, cloned))

    def testCompleteGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]
        
        cloned = self.solution.cloneGraph(node1)
        self.assertTrue(self._graphs_equal(node1, cloned))

    def testStarGraph(self):
        center = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        center.neighbors = [node2, node3, node4]
        node2.neighbors = [center]
        node3.neighbors = [center]
        node4.neighbors = [center]
        
        cloned = self.solution.cloneGraph(center)
        self.assertTrue(self._graphs_equal(center, cloned))

    def testSelfLoop(self):
        node = Node(1)
        node.neighbors = [node]
        
        cloned = self.solution.cloneGraph(node)
        self.assertIsNotNone(cloned)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 1)
        self.assertIs(cloned.neighbors[0], cloned)
        self.assertIsNot(cloned, node)

    def testMultiplePaths(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node3]
        node3.neighbors = []
        
        cloned = self.solution.cloneGraph(node1)
        self.assertTrue(self._graphs_equal(node1, cloned))

    def testClonedGraphIsIndependent(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        
        # Modify original graph
        node3 = Node(3)
        node1.neighbors.append(node3)
        
        # Cloned graph should not be affected
        self.assertEqual(len(cloned.neighbors), 1)
        self.assertEqual(cloned.neighbors[0].val, 2)


if __name__ == '__main__':
    unittest.main()