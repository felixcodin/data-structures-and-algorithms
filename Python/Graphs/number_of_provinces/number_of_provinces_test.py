import unittest
from number_of_provinces import Solution


class TestNumberOfProvinces(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_city(self):
        isConnected = [[1]]
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_two_cities_disconnected(self):
        isConnected = [
            [1, 0],
            [0, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)

    def test_two_cities_connected(self):
        isConnected = [
            [1, 1],
            [1, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_three_cities_one_isolated(self):
        isConnected = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)

    def test_chain_connectivity_transitive_single_province(self):
        # 0-1-2-3 connected as a chain => one province by transitive reachability
        isConnected = [
            [1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_two_components_of_two_cities_each(self):
        isConnected = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)

    def test_all_isolated_cities(self):
        isConnected = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 4)

    def test_fully_connected_five_cities(self):
        isConnected = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 1)

    def test_empty_matrix(self):
        isConnected = []
        self.assertEqual(self.solution.findCircleNum(isConnected), 0)

    def test_large_mixed_three_components(self):
        # Components: {0,1,2}, {3,4}, {5}
        isConnected = [
            [1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 3)

    def test_non_symmetric_matrix_current_behavior(self):
        # Problem input is typically symmetric, but this validates current DFS behavior.
        # Reachability from 0 visits 1; node 2 remains isolated => 2 provinces.
        isConnected = [
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        self.assertEqual(self.solution.findCircleNum(isConnected), 2)


if __name__ == "__main__":
    unittest.main()