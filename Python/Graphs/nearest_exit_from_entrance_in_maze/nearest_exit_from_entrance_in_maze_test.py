import unittest
from nearest_exit_from_entrance_in_maze import Solution


def clone_maze(maze):
    return [row[:] for row in maze]


class TestNearestExitFromEntranceInMaze(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_nearest_exit_one_step(self):
        maze = [
            ['+', '+', '.', '+'],
            ['.', '.', '.', '+'],
            ['+', '+', '+', '.']
        ]
        entrance = [1, 2]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 1)

    def test_example_nearest_exit_two_steps(self):
        maze = [
            ['+', '+', '+'],
            ['.', '.', '.'],
            ['+', '+', '+']
        ]
        entrance = [1, 0]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 2)

    def test_no_exit_enclosed(self):
        maze = [
            ['+', '+', '+'],
            ['+', '.', '+'],
            ['+', '+', '+']
        ]
        entrance = [1, 1]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), -1)

    def test_entrance_on_border_not_counted(self):
        maze = [['.', '+']]
        entrance = [0, 0]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), -1)

    def test_entrance_on_border_with_other_exit(self):
        maze = [['.', '.']]
        entrance = [0, 0]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 1)

    def test_single_cell_maze(self):
        maze = [['.']]
        entrance = [0, 0]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), -1)

    def test_multiple_exits_choose_nearest(self):
        maze = [
            ['.', '+', '.'],
            ['.', '.', '.'],
            ['.', '+', '.']
        ]
        entrance = [1, 1]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 1)

    def test_open_grid_center(self):
        maze = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        entrance = [1, 1]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 1)

    def test_corridor_path_length_three(self):
        maze = [
            ['+', '+', '+', '+', '+'],
            ['+', '.', '.', '.', '+'],
            ['+', '+', '+', '.', '+'],
            ['+', '.', '.', '.', '.'],
            ['+', '+', '+', '+', '+']
        ]
        entrance = [1, 1]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 5)

    def test_border_dot_unreachable(self):
        maze = [
            ['+', '+', '+', '.'],
            ['+', '.', '+', '+'],
            ['+', '.', '+', '+'],
            ['+', '.', '.', '+']
        ]
        entrance = [1, 1]
        self.assertEqual(self.solution.nearestExit(clone_maze(maze), entrance), 2)

    def test_repeat_calls_with_fresh_copies(self):
        maze = [
            ['+', '+', '.'],
            ['.', '.', '.'],
            ['+', '+', '+']
        ]
        entrance = [1, 1]
        first = self.solution.nearestExit(clone_maze(maze), entrance)
        second = self.solution.nearestExit(clone_maze(maze), entrance)
        self.assertEqual(first, 1)
        self.assertEqual(second, 1)


if __name__ == "__main__":
    unittest.main()