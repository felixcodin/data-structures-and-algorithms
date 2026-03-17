import unittest
from even_odd_linked_list import Solution, ListNode


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head, limit=1000):
    values = []
    current = head
    steps = 0
    while current:
        values.append(current.val)
        current = current.next
        steps += 1
        if steps > limit:
            raise AssertionError("Linked list traversal exceeded limit; possible cycle.")
    return values


class TestEvenOddLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testEmptyList(self):
        head = build_linked_list([])
        result = self.solution.oddEvenList(head)
        self.assertIsNone(result)

    def testSingleNode(self):
        head = build_linked_list([1])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def testTwoNodes(self):
        head = build_linked_list([1, 2])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def testThreeNodes(self):
        head = build_linked_list([1, 2, 3])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 3, 2])

    def testFourNodes(self):
        head = build_linked_list([1, 2, 3, 4])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 3, 2, 4])

    def testFiveNodes(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 3, 5, 2, 4])

    def testSixNodes(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [1, 3, 5, 2, 4, 6])

    def testLeetCodeStyleMixedValues(self):
        head = build_linked_list([2, 1, 3, 5, 6, 4, 7])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [2, 3, 6, 7, 1, 5, 4])

    def testNegativeAndZeroValues(self):
        head = build_linked_list([0, -1, -2, -3, -4])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [0, -2, -4, -1, -3])

    def testDuplicateValues(self):
        head = build_linked_list([9, 9, 9, 9, 9, 9])
        result = self.solution.oddEvenList(head)
        self.assertEqual(linked_list_to_list(result), [9, 9, 9, 9, 9, 9])

    def testLongList(self):
        values = list(range(1, 11))  # 1..10
        head = build_linked_list(values)
        result = self.solution.oddEvenList(head)
        expected = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        self.assertEqual(linked_list_to_list(result), expected)

    def testHeadIdentityPreservedForNonEmptyList(self):
        head = build_linked_list([10, 20, 30, 40])
        original_head = head
        result = self.solution.oddEvenList(head)
        self.assertIs(result, original_head)
        self.assertEqual(linked_list_to_list(result), [10, 30, 20, 40])

    def testTailIsLastEvenNodeWhenEvenCount(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        result = self.solution.oddEvenList(head)
        result_list = linked_list_to_list(result)
        self.assertEqual(result_list, [1, 3, 5, 7, 2, 4, 6, 8])
        self.assertEqual(result_list[-1], 8)


if __name__ == "__main__":
    unittest.main()