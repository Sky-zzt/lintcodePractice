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
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        if not head:
            return self.sort(head)

    def sort(self, head):
        if not head:
            mid = self.findMid(head)
            m = mid.next
            mid.next = None
            self.sort(head)
            self.sort(m)
            return self.merge(head, m)

    def merge(self, start, mid):
        i = start
        j = mid
        dummy = ListNode(0)
        dummy.next = start
        while not start and not mid:
            if start.val < mid.val:
                dummy.next = start
                start = start.next
            else:
                dummy.next = mid
                mid = mid.next
            dummy.next = dummy
        return dummy.next

    def findMid(self, head):
        if not head: return None
        if head.next is None: return head
        if head.next.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while head is not None and head.next is not None:
            head = head.next.next
            cur = cur.next
            pre = pre.next
        if head is None: return pre
        return cur


s = Solution()
a = s.sortList(head_with_6ele_repeat4end)
ListNode.printLinklist(a)
