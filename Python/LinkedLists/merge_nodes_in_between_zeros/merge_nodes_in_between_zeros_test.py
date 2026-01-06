import unittest
from merge_nodes_in_between_zeros import Solution, ListNode

class TestMergeNodesInBetweenZeros(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def testExampleCase1(self):
        head = self.array_to_list([0, 3, 1, 0, 4, 5, 2, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [4, 11])

    def testExampleCase2(self):
        head = self.array_to_list([0, 1, 0, 3, 0, 2, 2, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [1, 3, 4])

    def testSingleSegment(self):
        head = self.array_to_list([0, 5, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [5])

    def testMultipleNodesInSegment(self):
        head = self.array_to_list([0, 1, 2, 3, 4, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [10])

    def testTwoSegments(self):
        head = self.array_to_list([0, 1, 0, 2, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [1, 2])

    def testEmptyList(self):
        head = None
        result = self.solution.mergeNodes(head)
        self.assertIsNone(result)

    def testLargerValues(self):
        head = self.array_to_list([0, 100, 200, 0, 50, 50, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [300, 100])

    def testThreeSegments(self):
        head = self.array_to_list([0, 1, 1, 0, 2, 2, 0, 3, 3, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [2, 4, 6])

    def testSingleValueSegments(self):
        head = self.array_to_list([0, 5, 0, 10, 0, 15, 0])
        result = self.solution.mergeNodes(head)
        self.assertEqual(self.list_to_array(result), [5, 10, 15])

if __name__ == '__main__':
    unittest.main()