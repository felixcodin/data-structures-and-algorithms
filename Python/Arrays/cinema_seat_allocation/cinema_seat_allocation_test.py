import unittest
from cinema_seat_allocation import Solution


class TestCinemaSeatAllocation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_reserved_seats(self):
        """All seats available, 2 families per row"""
        result = self.solution.maxNumberOfFamilies(3, [])
        self.assertEqual(result, 6)  # 3 rows * 2 families

    def test_single_row_no_reservation(self):
        """Single row with no reservation, 2 families can sit"""
        result = self.solution.maxNumberOfFamilies(1, [])
        self.assertEqual(result, 2)

    def test_single_row_blocking_left(self):
        """Single row, seat 2 reserved (blocks left placement only)"""
        result = self.solution.maxNumberOfFamilies(1, [[1, 2]])
        self.assertEqual(result, 1)  # mid or right still possible

    def test_single_row_blocking_all(self):
        """Single row, multiple seats reserved blocking all placements"""
        result = self.solution.maxNumberOfFamilies(1, [[1, 3], [1, 5], [1, 7], [1, 9]])
        self.assertEqual(result, 0)  # All placements blocked

    def test_single_row_blocking_all_consecutive(self):
        """Single row, consecutive seats 2-9 reserved (all placements blocked)"""
        result = self.solution.maxNumberOfFamilies(1, [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]])
        self.assertEqual(result, 0)

    def test_two_rows_one_reserved(self):
        """2 rows, 1 seat reserved in row 1"""
        result = self.solution.maxNumberOfFamilies(2, [[1, 5]])
        self.assertEqual(result, 3)  # Row 1: 1 family, Row 2: 2 families

    def test_multiple_rows_reserved_seats(self):
        """3 rows with mixed reservations"""
        # Row 1: seat 5 reserved (blocks left and mid) → subtract 1
        # Row 2: no reservation
        # Row 3: seats 4 and 8 reserved (blocks all) → subtract 2
        result = self.solution.maxNumberOfFamilies(3, [[1, 5], [3, 4], [3, 8]])
        self.assertEqual(result, 3)  # Start: 6, -1 for row 1, -2 for row 3

    def test_large_n_few_reserved(self):
        """Large number of rows with few reserved seats"""
        result = self.solution.maxNumberOfFamilies(1000, [[1, 2]])
        self.assertEqual(result, 1999)  # 999 rows * 2 + 1 row * 1

    def test_example_case_1(self):
        """LeetCode example: n=3, reservedSeats=[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]"""
        result = self.solution.maxNumberOfFamilies(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]])
        self.assertEqual(result, 4)

    def test_only_unreserved_rows_count(self):
        """Verify that only rows with reservations are processed"""
        result = self.solution.maxNumberOfFamilies(5, [[2, 5]])
        self.assertEqual(result, 9)  # 4 rows * 2 + 1 row * 1

    def test_blocking_left_and_mid(self):
        """Seats blocking all placements"""
        # Seats 3-6 block left (2-5), mid (4-7), and right (6-9)
        result = self.solution.maxNumberOfFamilies(1, [[1, 3], [1, 4], [1, 5], [1, 6]])
        self.assertEqual(result, 0)  # All placements blocked, subtract 2 from initial 2


if __name__ == "__main__":
    unittest.main()
