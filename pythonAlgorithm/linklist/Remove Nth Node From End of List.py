"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from linklist.list_node import ListNode


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    # todo 先让快指针走n步，然后快慢一起走，走到头的时候慢指针指向的点删掉。
    def removeNthFromEnd(self, head, n):
        # write your code here
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(1, n + 1):
            head = head.next
        while head is not None:
            head = head.next
            cur = cur.next
            pre = pre.next
        pre.next = cur.next
        return dummy.next
