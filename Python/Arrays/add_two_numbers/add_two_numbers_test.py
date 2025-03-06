import unittest
from add_two_numbers import Solution
from add_two_numbers import ListNode

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def listToLinkedList(self, lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    def linkedListToList(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst
    def testBothListsHaveTheSameLength(self):
        l1 = self.listToLinkedList([2, 4, 3])
        l2 = self.listToLinkedList([5, 6, 4])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [7, 0, 8])
    def testDifferentLengthsNoCarry(self):
        l1 = self.listToLinkedList([1, 2])
        l2 = self.listToLinkedList([9])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [0, 3])
    def testDifferentLengthWithCarry(self):
        l1 = self.listToLinkedList([9, 9])
        l2 = self.listToLinkedList([1])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [0, 0, 1])
    def testBothListAreEmpty(self):
        l1 = self.listToLinkedList([])
        l2 = self.listToLinkedList([])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
    def testOneListIsEmpty(self):
        l1 = self.listToLinkedList([0])
        l2 = self.listToLinkedList([1, 2, 5])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [1, 2, 5])
    def testBothListsHaveOneElement(self):
        l1 = self.listToLinkedList([5])
        l2 = self.listToLinkedList([5])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [0, 1])
    def testCarryOverMultipleDigits(self):
        l1 = self.listToLinkedList([9, 9, 9])
        l2 = self.listToLinkedList([1])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [0, 0, 0, 1])
    def testLargeNumber(self):
        l1 = self.listToLinkedList([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        l2 = self.listToLinkedList([5, 6, 4])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    def testLeadingZeroOnTheResult(self):
        l1 = self.listToLinkedList([0, 0, 1])
        l2 = self.listToLinkedList([0, 0, 9])
        res = self.linkedListToList(self.solution.addTwoNumber(l1, l2))
        self.assertEqual(res, [0, 0, 0, 1])
    
if __name__ == '__main__':
    unittest.main()