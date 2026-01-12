import unittest
from reorder_linked_list import Solution, ListNode

class TestReorderLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def testBasicCase(self):
        head = self.array_to_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 4, 2, 3])

    def testFiveElements(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 5, 2, 4, 3])

    def testSingleElement(self):
        head = self.array_to_list([1])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1])

    def testTwoElements(self):
        head = self.array_to_list([1, 2])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 2])

    def testThreeElements(self):
        head = self.array_to_list([1, 2, 3])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 3, 2])

    def testEmptyList(self):
        head = None
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [])

    def testSixElements(self):
        head = self.array_to_list([1, 2, 3, 4, 5, 6])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 6, 2, 5, 3, 4])

    def testSevenElements(self):
        head = self.array_to_list([1, 2, 3, 4, 5, 6, 7])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [1, 7, 2, 6, 3, 5, 4])

    def testLargeValues(self):
        head = self.array_to_list([10, 20, 30, 40, 50])
        self.solution.reorderList(head)
        result = self.list_to_array(head)
        self.assertEqual(result, [10, 50, 20, 40, 30])


if __name__ == '__main__':
    unittest.main()