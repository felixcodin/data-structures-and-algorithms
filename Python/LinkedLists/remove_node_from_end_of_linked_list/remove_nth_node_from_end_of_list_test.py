import unittest
from remove_nth_node_from_end_of_list import Solution, ListNode

class TestRemoveNthFromEnd(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head):
        """Helper function to convert linked list to array"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr):
        """Helper function to convert array to linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def testRemoveLastNode(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 4])

    def testRemoveFirstNode(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 5)
        self.assertEqual(self.list_to_array(result), [2, 3, 4, 5])

    def testRemoveMiddleNode(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.list_to_array(result), [1, 2, 4, 5])

    def testSingleNodeList(self):
        head = self.array_to_list([1])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertIsNone(result)

    def testTwoNodeListRemoveFirst(self):
        head = self.array_to_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.list_to_array(result), [2])

    def testTwoNodeListRemoveSecond(self):
        head = self.array_to_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.list_to_array(result), [1])

    def testRemoveSecondToLast(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 5])

    def testThreeNodeList(self):
        head = self.array_to_list([1, 2, 3])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.list_to_array(result), [1, 3])

    def testLargerList(self):
        head = self.array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = self.solution.removeNthFromEnd(head, 4)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 4, 5, 6, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()