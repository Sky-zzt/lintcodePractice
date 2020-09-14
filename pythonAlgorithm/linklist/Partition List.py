"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from linklist.list_node import ListNode, head_with_6ele_repeat4end


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if not head: return 0
        Leftdummy = ListNode(0)
        rightdummy = ListNode(0)
        left = Leftdummy
        right = rightdummy
        while head is not None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = rightdummy.next
        return Leftdummy.next


s = Solution()
s.partition(head_with_6ele_repeat4end, 2)
