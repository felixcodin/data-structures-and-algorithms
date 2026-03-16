import unittest
from delete_the_middle_node_of_a_linked_list import (
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


def linked_list_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


class TestDeleteMiddleNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSingleNodeReturnsNone(self):
        head = build_linked_list([1])
        result = self.solution.deleteMiddle(head)
        self.assertIsNone(result)

    def testTwoNodesRemovesSecond(self):
        head = build_linked_list([1, 2])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def testThreeNodesRemovesMiddle(self):
        head = build_linked_list([1, 2, 3])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [1, 3])

    def testFourNodesRemovesIndexNBy2(self):
        head = build_linked_list([1, 2, 3, 4])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 4])

    def testFiveNodesRemovesThird(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 4, 5])

    def testSixNodesRemovesFourth(self):
        head = build_linked_list([10, 20, 30, 40, 50, 60])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [10, 20, 30, 50, 60])

    def testDuplicateValuesRemovesByPosition(self):
        head = build_linked_list([7, 7, 7, 7, 7])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [7, 7, 7, 7])

    def testNegativeAndZeroValues(self):
        head = build_linked_list([-3, -2, -1, 0, 1])
        result = self.solution.deleteMiddle(head)
        self.assertEqual(linked_list_to_list(result), [-3, -2, 0, 1])

    def testLargeList(self):
        values = list(range(1, 101))  # 1..100
        head = build_linked_list(values)
        result = self.solution.deleteMiddle(head)
        expected = values[:50] + values[51:]  # remove index 50 (value 51)
        self.assertEqual(linked_list_to_list(result), expected)

    def testReturnedHeadIsOriginalHeadForLengthGreaterThanOne(self):
        head = build_linked_list([5, 6, 7, 8])
        original_head = head
        result = self.solution.deleteMiddle(head)
        self.assertIs(result, original_head)
        self.assertEqual(linked_list_to_list(result), [5, 6, 8])


if __name__ == "__main__":
    unittest.main()