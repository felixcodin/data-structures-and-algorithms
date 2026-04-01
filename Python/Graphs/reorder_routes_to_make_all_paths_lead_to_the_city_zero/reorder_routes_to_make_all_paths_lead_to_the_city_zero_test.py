import unittest
from reorder_routes_to_make_all_paths_lead_to_the_city_zero import Solution


class TestReorderRoutesToCityZero(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_city_no_connections(self):
        n = 1
        connections = []
        self.assertEqual(self.solution.minReorder(n, connections), 0)

    def test_leetcode_example_1(self):
        n = 6
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
        self.assertEqual(self.solution.minReorder(n, connections), 3)

    def test_leetcode_example_2(self):
        n = 5
        connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
        self.assertEqual(self.solution.minReorder(n, connections), 2)

    def test_leetcode_example_3_all_already_to_zero(self):
        n = 3
        connections = [[1, 0], [2, 0]]
        self.assertEqual(self.solution.minReorder(n, connections), 0)

    def test_chain_all_away_from_zero(self):
        # 0->1->2->3->4, all must be reversed
        n = 5
        connections = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.minReorder(n, connections), 4)

    def test_chain_all_toward_zero(self):
        # 4->3->2->1->0, none must be reversed
        n = 5
        connections = [[1, 0], [2, 1], [3, 2], [4, 3]]
        self.assertEqual(self.solution.minReorder(n, connections), 0)

    def test_star_outward_from_zero(self):
        # 0->1, 0->2, 0->3, 0->4: all need reversing
        n = 5
        connections = [[0, 1], [0, 2], [0, 3], [0, 4]]
        self.assertEqual(self.solution.minReorder(n, connections), 4)

    def test_star_inward_to_zero(self):
        # 1->0, 2->0, 3->0, 4->0: already correct
        n = 5
        connections = [[1, 0], [2, 0], [3, 0], [4, 0]]
        self.assertEqual(self.solution.minReorder(n, connections), 0)

    def test_mixed_tree_partial_reorder(self):
        # Undirected structure edges:
        # 0-1, 1-2, 1-3, 3-4, 4-5
        # Directed:
        # 0->1 (wrong), 2->1 (ok), 1->3 (wrong), 4->3 (ok), 4->5 (wrong)
        # Required reversals: (0,1), (1,3), (4,5) => 3
        n = 6
        connections = [[0, 1], [2, 1], [1, 3], [4, 3], [4, 5]]
        self.assertEqual(self.solution.minReorder(n, connections), 3)

    def test_connection_order_does_not_change_result(self):
        n = 6
        connections_a = [[0, 1], [2, 1], [1, 3], [4, 3], [4, 5]]
        connections_b = [[4, 5], [1, 3], [4, 3], [0, 1], [2, 1]]
        result_a = self.solution.minReorder(n, connections_a)
        result_b = self.solution.minReorder(n, connections_b)
        self.assertEqual(result_a, 3)
        self.assertEqual(result_b, 3)


if __name__ == "__main__":
    unittest.main()