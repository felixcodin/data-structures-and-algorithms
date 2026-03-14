import unittest

from number_of_recent_calls import RecentCounter


class TestRecentCounter(unittest.TestCase):
    def test_leetcode_example(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(100), 2)
        self.assertEqual(counter.ping(3001), 3)
        self.assertEqual(counter.ping(3002), 3)

    def test_single_ping(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(500), 1)

    def test_boundary_time_is_included(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(3001), 2)

    def test_call_older_than_boundary_is_removed(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(3002), 1)

    def test_multiple_old_calls_removed_at_once(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(2), 2)
        self.assertEqual(counter.ping(3), 3)
        self.assertEqual(counter.ping(4000), 1)

    def test_all_calls_within_window_are_counted(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1000), 1)
        self.assertEqual(counter.ping(1500), 2)
        self.assertEqual(counter.ping(2000), 3)
        self.assertEqual(counter.ping(2500), 4)
        self.assertEqual(counter.ping(4000), 5)

    def test_window_slides_over_several_pings(self):
        counter = RecentCounter()

        calls = [1, 100, 1000, 3000, 3001, 6000]
        expected = [1, 2, 3, 4, 5, 3]

        for time, count in zip(calls, expected):
            self.assertEqual(counter.ping(time), count)

    def test_repeated_pings_same_timestamp(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(3000), 1)
        self.assertEqual(counter.ping(3000), 2)
        self.assertEqual(counter.ping(3000), 3)
        self.assertEqual(counter.ping(6000), 4)

    def test_large_gaps_leave_only_recent_calls(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(10000), 1)
        self.assertEqual(counter.ping(12000), 2)
        self.assertEqual(counter.ping(13001), 2)

    def test_state_persists_across_many_calls(self):
        counter = RecentCounter()

        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(1000), 2)
        self.assertEqual(counter.ping(2000), 3)
        self.assertEqual(counter.ping(3000), 4)
        self.assertEqual(counter.ping(4001), 3)
        self.assertEqual(counter.ping(5000), 4)


if __name__ == '__main__':
    unittest.main()