#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumber(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry == 1:
            total = 0

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            total += 1 if carry == 1 else 0
            carry = total // 10
            dummy.next = ListNode(total % 10)
            dummy = dummy.next
        
        return res.next

def test_addTwoNumbers():
    def list_to_linkedlist(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def linkedlist_to_list(node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    solution = Solution()

    # Test case 1: Both lists have the same length
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8]

    # Test case 2: Different lengths, no carry
    l1 = list_to_linkedlist([1, 2])
    l2 = list_to_linkedlist([9])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 3]

    # Test case 3: Different lengths, with carry
    l1 = list_to_linkedlist([9, 9])
    l2 = list_to_linkedlist([1])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 1]

    # Test case 4: Both lists are empty
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == []

    # Test case 5: One list is empty
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([1, 2, 3])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [1, 2, 3]

    # Test case 6: Both lists have one element
    l1 = list_to_linkedlist([5])
    l2 = list_to_linkedlist([5])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 1]

    # Test case 7: Carry over multiple digits
    l1 = list_to_linkedlist([9, 9, 9])
    l2 = list_to_linkedlist([1])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 0, 1]

    # Test case 8: Large numbers
    l1 = list_to_linkedlist([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    # Test case 9: Leading zeros in the result
    l1 = list_to_linkedlist([0, 0, 1])
    l2 = list_to_linkedlist([0, 0, 9])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 0, 0, 1]

    # Test case 10: Single digit with carry
    l1 = list_to_linkedlist([5])
    l2 = list_to_linkedlist([5])
    result = solution.addTwoNumber(l1, l2)
    assert linkedlist_to_list(result) == [0, 1]

# Run the test cases
test_addTwoNumbers()
print("All test cases passed!")
