import unittest
from maximum_twin_sum_of_a_linked_list import (
    ListNode,
    Solution,
)


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for val in values[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


class TestMaximumTwinSumOfLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        head = build_linked_list([5, 4, 2, 1])
        self.assertEqual(self.solution.pairSum(head), 6)

    def test_leetcode_example_2(self):
        head = build_linked_list([4, 2, 2, 3])
        self.assertEqual(self.solution.pairSum(head), 7)

    def test_leetcode_example_3(self):
        head = build_linked_list([1, 100000])
        self.assertEqual(self.solution.pairSum(head), 100001)

    def test_min_even_length(self):
        head = build_linked_list([1, 2])
        self.assertEqual(self.solution.pairSum(head), 3)

    def test_all_equal_values(self):
        head = build_linked_list([7, 7, 7, 7, 7, 7])
        self.assertEqual(self.solution.pairSum(head), 14)

    def test_increasing_values(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(self.solution.pairSum(head), 7)

    def test_decreasing_values(self):
        head = build_linked_list([9, 8, 7, 6, 5, 4])
        self.assertEqual(self.solution.pairSum(head), 13)

    def test_mixed_values(self):
        head = build_linked_list([10, 1, 9, 2, 8, 3, 7, 4])
        self.assertEqual(self.solution.pairSum(head), 14)

    def test_maximum_not_from_first_pair(self):
        head = build_linked_list([1, 2, 100, 3, 4, 5])
        # Twin sums: (1+5)=6, (2+4)=6, (100+3)=103
        self.assertEqual(self.solution.pairSum(head), 103)

    def test_large_even_list(self):
        values = list(range(1, 101))  # 1..100
        head = build_linked_list(values)
        # Every twin sum is 101
        self.assertEqual(self.solution.pairSum(head), 101)

    def test_zeros_only(self):
        head = build_linked_list([0, 0, 0, 0])
        self.assertEqual(self.solution.pairSum(head), 0)

    def test_single_high_middle_pairs(self):
        head = build_linked_list([1, 1, 50, 50, 1, 1])
        # Twin sums: 2, 2, 100
        self.assertEqual(self.solution.pairSum(head), 100)


if __name__ == "__main__":
    unittest.main()