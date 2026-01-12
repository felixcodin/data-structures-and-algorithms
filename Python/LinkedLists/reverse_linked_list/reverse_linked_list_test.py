import unittest
from reverse_linked_list import Solution, ListNode

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head: ListNode) -> list:
        """Helper method to convert linked list to array for easy comparison"""
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def array_to_list(self, arr: list) -> ListNode:
        """Helper method to convert array to linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def testBasicCase(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [5, 4, 3, 2, 1])

    def testSingleNode(self):
        head = self.array_to_list([1])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [1])

    def testEmptyList(self):
        head = None
        result = self.solution.reverseList(head)
        self.assertIsNone(result)

    def testTwoNodes(self):
        head = self.array_to_list([1, 2])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [2, 1])

    def testThreeNodes(self):
        head = self.array_to_list([1, 2, 3])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [3, 2, 1])

    def testLongerList(self):
        head = self.array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def testNegativeValues(self):
        head = self.array_to_list([-1, -2, -3])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [-3, -2, -1])

    def testMixedValues(self):
        head = self.array_to_list([0, -5, 10, -3, 7])
        result = self.solution.reverseList(head)
        self.assertEqual(self.list_to_array(result), [7, -3, 10, -5, 0])


if __name__ == '__main__':
    unittest.main()