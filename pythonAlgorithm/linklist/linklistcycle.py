"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        if not head: return False
        cur = head
        while head is not None and head.next is not None:
            cur = cur.next
            head = head.next.next
            if id(cur) == id(head):
                return True
        return False
