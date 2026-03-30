import unittest
from keys_and_rooms import Solution


class TestKeysAndRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_room_no_keys(self):
        rooms = [[]]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_simple_chain_all_reachable(self):
        rooms = [[1], [2], [3], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_unreachable_disconnected_rooms(self):
        rooms = [[1], [], [3], []]
        self.assertFalse(self.solution.canVisitAllRooms(rooms))

    def test_leetcode_example_true(self):
        rooms = [[1], [2], [3], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_leetcode_example_false(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        self.assertFalse(self.solution.canVisitAllRooms(rooms))

    def test_cycle_with_full_reachability(self):
        rooms = [[1], [2], [0, 3], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_cycle_without_full_reachability(self):
        rooms = [[1], [0], []]
        self.assertFalse(self.solution.canVisitAllRooms(rooms))

    def test_duplicate_keys(self):
        rooms = [[1, 1, 1], [2, 2], [3], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_self_keys_present(self):
        rooms = [[0, 1], [1, 2], [2]]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_room_zero_has_all_keys(self):
        rooms = [[1, 2, 3, 4], [], [], [], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_dead_end_branch_still_reachable(self):
        rooms = [[1, 2], [3], [], [4], []]
        self.assertTrue(self.solution.canVisitAllRooms(rooms))

    def test_larger_graph_with_unreachable_component(self):
        rooms = [[1, 2], [3], [3], [4], [], [6], []]
        self.assertFalse(self.solution.canVisitAllRooms(rooms))

    def test_empty_input_raises_index_error_current_behavior(self):
        with self.assertRaises(IndexError):
            self.solution.canVisitAllRooms([])


if __name__ == "__main__":
    unittest.main()