"""
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


class ListNode:
    """Linked list class"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Solution class"""
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Removes elements of a linked list that are equal to a
        given value
        Args:
            head: first node of the linked list
            val: value to delete in linked list
        Return:
            the updated linked list
        """
        curr = head
        prev = None

        while curr:
            temp = curr
            if head.val == val:
                head = head.next
                temp = None
                curr = head
            elif curr.val == val:
                prev.next = curr.next
                curr = curr.next
                temp = None
            else:
                prev = curr
                curr = curr.next

        return head
